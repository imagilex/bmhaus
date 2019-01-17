from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError

import json

from .models import (
    Vehiculo,
    DoctoOrdenReparacion,
    AvanceEnFlujo,
    doctoordenreparacion_upload_to,
    avanceenflujo_upload_to,
    newIdentificadorForDoctoOrdenReparacion)
from .forms import (
    FrmDoctoOrdenReparacion,
    FrmDoctoOrdenReparacionGenerales01,
    FrmDoctoOrdenReparacionGenerales02,
    FrmDoctoOrdenReparacionExteriores,
    FrmDoctoOrdenReparacionInteriores,
    FrmDoctoOrdenReparacionAccesorios,
    FrmDoctoOrdenReparacionComponentesMecanicos,
    FrmDoctoOrdenReparacionFirmas,
    FrmAvanceEnFlujo)
from .functions import merge_flujo_acciones
from flujo.models import (
    Flujo, Estado, Accion, InstanciaFlujo, InstanciaHistoriaDetalle)
from routines.mkitsafe import valida_acceso
from routines.utils import move_uploaded_file, hipernormalize
from initsys.models import Usr


@valida_acceso([
    'vehiculo.agregar_servicios_vehiculo',
    'vehiculo.actualizar_servicios_vehiculo'])
def new_from_taller(request, pkvehiculo):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    toolbar = []
    vehiculo = Vehiculo.objects.get(pk=pkvehiculo)
    flujo = Flujo.objects.get(name='temporal_operaciones')
    estado_inicial = flujo.estados.get(name='inicio')
    accion = estado_inicial.acciones_ejecutar.filter(
        name='recibir_vehiculo_en_taller')[0]
    instanciaflujo = InstanciaFlujo.objects.create(
        flujo=flujo,
        tipo_instancia='Vehiculo',
        estado_actual=estado_inicial,
        extra_data='{"idobjeto":' + str(vehiculo.pk) + '}',
        created_by=usuario,
        updated_by=usuario)
    return render(
        request,
        'app/servicios/new.html',
        {
            'menu_main': usuario.main_menu_struct(),
            'titulo': accion.nombre,
            'titulo_descripcion': "{}/{}".format(
                vehiculo.propietario, vehiculo),
            'toolbar': toolbar,
            'accion': accion,
            'instanciaflujo': instanciaflujo,
            'vehiculo': vehiculo,
            'titulo_frm_1': '',
            'frm1': FrmDoctoOrdenReparacionGenerales01(),
            'titulo_frm_2': '',
            'frm2': FrmDoctoOrdenReparacionGenerales02(),
            'titulo_frm_3': 'Exteriores',
            'frm3': FrmDoctoOrdenReparacionExteriores(),
            'titulo_frm_4': 'Interiores',
            'frm4': FrmDoctoOrdenReparacionInteriores(),
            'titulo_frm_5': 'Accesorios',
            'frm5': FrmDoctoOrdenReparacionAccesorios(),
            'titulo_frm_6': 'Componentes Mecánicos',
            'frm6': FrmDoctoOrdenReparacionComponentesMecanicos(),
            'titulo_frm_7': '',
            'frm7': FrmDoctoOrdenReparacionFirmas(),
        }
    )


@valida_acceso([
    'vehiculo.agregar_servicios_vehiculo',
    'vehiculo.actualizar_servicios_vehiculo'])
def new_from_dir_particular(request, pkvehiculo):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    toolbar = []
    vehiculo = Vehiculo.objects.get(pk=pkvehiculo)
    flujo = Flujo.objects.get(name='temporal_operaciones')
    estado_inicial = flujo.estados.get(name='inicio')
    accion = estado_inicial.acciones_ejecutar.filter(
        name='recibir_vehiculo_en_domicilio')[0]
    instanciaflujo = InstanciaFlujo.objects.create(
        flujo=flujo,
        tipo_instancia='Vehiculo',
        estado_actual=estado_inicial,
        extra_data='{"idobjeto":' + str(vehiculo.pk) + '}',
        created_by=usuario,
        updated_by=usuario)
    return render(
        request,
        'app/servicios/new.html',
        {
            'menu_main': usuario.main_menu_struct(),
            'titulo': accion.nombre,
            'titulo_descripcion': "{}/{}".format(
                vehiculo.propietario, vehiculo),
            'toolbar': toolbar,
            'accion': accion,
            'instanciaflujo': instanciaflujo,
            'vehiculo': vehiculo,
            'titulo_frm_1': '',
            'frm1': FrmDoctoOrdenReparacionGenerales01(),
            'titulo_frm_2': '',
            'frm2': FrmDoctoOrdenReparacionGenerales02(),
            'titulo_frm_3': 'Exteriores',
            'frm3': FrmDoctoOrdenReparacionExteriores(),
            'titulo_frm_4': 'Interiores',
            'frm4': FrmDoctoOrdenReparacionInteriores(),
            'titulo_frm_5': 'Accesorios',
            'frm5': FrmDoctoOrdenReparacionAccesorios(),
            'titulo_frm_6': 'Componentes Mecánicos',
            'frm6': FrmDoctoOrdenReparacionComponentesMecanicos(),
            'titulo_frm_7': '',
            'frm7': FrmDoctoOrdenReparacionFirmas(),
        }
    )


@valida_acceso([
    'vehiculo.agregar_servicios_vehiculo',
    'vehiculo.actualizar_servicios_vehiculo'])
def executeaccion(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    toolbar = []
    rendering = True
    render_to = ''
    render_params = {}
    if "POST" == request.method:
        if "move_to" == request.POST.get("action"):
            accion = Accion.objects.get(pk=request.POST.get("accion"))
            instanciaflujo = InstanciaFlujo.objects.get(
                pk=request.POST.get("instanciaflujo"))
            vehiculo = Vehiculo.objects.get(
                pk=request.POST.get("vehiculo"))
            if instanciaflujo.estado_actual.es_inicial is True:
                frm = FrmDoctoOrdenReparacion(data=request.POST)
                frmGral1 = FrmDoctoOrdenReparacionGenerales01(
                    data=request.POST)
                frmGral2 = FrmDoctoOrdenReparacionGenerales02(
                    data=request.POST)
                frmExt = FrmDoctoOrdenReparacionExteriores(
                    data=request.POST)
                frmInt = FrmDoctoOrdenReparacionInteriores(
                    data=request.POST)
                frmAcc = FrmDoctoOrdenReparacionAccesorios(
                    data=request.POST)
                frmCMex = FrmDoctoOrdenReparacionComponentesMecanicos(
                    data=request.POST)
                frmSign = FrmDoctoOrdenReparacionFirmas(
                    data=request.POST)
                if frm.is_valid():
                    obj = frm.save(commit=False)
                    obj.vehiculo = vehiculo
                    obj.created_by = usuario
                    obj.updated_by = usuario
                    obj.identificador = newIdentificadorForDoctoOrdenReparacion()
                    if request.FILES.get('fotografia_kilometros'):
                        obj.fotografia_kilometros = move_uploaded_file(
                            request.FILES.get('fotografia_kilometros'),
                            doctoordenreparacion_upload_to)
                    if request.FILES.get('fotografia_tanque_de_gasolina'):
                        obj.fotografia_tanque_de_gasolina = move_uploaded_file(
                            request.FILES.get(
                                'fotografia_tanque_de_gasolina'),
                            doctoordenreparacion_upload_to)
                    if request.FILES.get('fotografia_superior'):
                        obj.fotografia_superior = move_uploaded_file(
                            request.FILES.get('fotografia_superior'),
                            doctoordenreparacion_upload_to)
                    if request.FILES.get('fotografia_frente'):
                        obj.fotografia_frente = move_uploaded_file(
                            request.FILES.get('fotografia_frente'),
                            doctoordenreparacion_upload_to)
                    if request.FILES.get('fotografia_trasera'):
                        obj.fotografia_trasera = move_uploaded_file(
                            request.FILES.get('fotografia_trasera'),
                            doctoordenreparacion_upload_to)
                    if request.FILES.get('fotografia_lateral_izquierdo'):
                        obj.fotografia_lateral_izquierdo = \
                            move_uploaded_file(
                                request.FILES.get(
                                    'fotografia_lateral_izquierdo'),
                                doctoordenreparacion_upload_to)
                    if request.FILES.get('fotografia_lateral_derecho'):
                        obj.fotografia_lateral_derecho = \
                            move_uploaded_file(
                                request.FILES.get(
                                    'fotografia_lateral_derecho'),
                                doctoordenreparacion_upload_to)
                    if request.FILES.get(
                            'firma_del_prestador_del_servicio'):
                        obj.firma_del_prestador_del_servicio = \
                            move_uploaded_file(
                                request.FILES.get(
                                    'firma_del_prestador_del_servicio'),
                                doctoordenreparacion_upload_to)
                    if request.FILES.get('firma_del_consumidor'):
                        obj.firma_del_consumidor = move_uploaded_file(
                            request.FILES.get('firma_del_consumidor'),
                            doctoordenreparacion_upload_to)
                    obj.save()
                    historia = instanciaflujo.historia.create(
                        accion=accion,
                        extra_data=instanciaflujo.extra_data,
                        created_by=usuario,
                        updated_by=usuario
                    )
                    instanciaflujo.estado_actual = accion.estado_final
                    if (accion.estado_final.es_final is True
                            or accion.estado_final.es_cancelacion is True):
                        instanciaflujo.terminado = True
                    historia.historia_detalle.create(
                        iddocumento_generado=obj.pk,
                        tipo_documento_generado='DoctoOrdenReparacion',
                        extra_data=historia.extra_data,
                        created_by=usuario,
                        updated_by=usuario,
                    )
                    instanciaflujo.save()
                    rendering = False
                    render_to = 'doctoordenreparacion_see',
                    render_params = {'pk': obj.pk}
                else:
                    render_to = 'app/servicios/new.html'
                    render_params = {
                        'menu_main': usuario.main_menu_struct(),
                        'titulo': accion.nombre,
                        'titulo_descripcion': "{}/{}".format(
                            vehiculo.propietario, vehiculo),
                        'toolbar': toolbar,
                        'accion': accion,
                        'instanciaflujo': instanciaflujo,
                        'vehiculo': vehiculo,
                        'titulo_frm_1': '',
                        'frm1': frmGral1,
                        'titulo_frm_2': '',
                        'frm2': frmGral2,
                        'titulo_frm_3': 'Exteriores',
                        'frm3': frmExt,
                        'titulo_frm_4': 'Interiores',
                        'frm4': frmInt,
                        'titulo_frm_5': 'Accesorios',
                        'frm5': frmAcc,
                        'titulo_frm_6': 'Componentes Mecánicos',
                        'frm6': frmCMex,
                        'titulo_frm_7': '',
                        'frm7': frmSign,
                    }
            else:
                frm = FrmAvanceEnFlujo(data=request.POST)
                if frm.is_valid():
                    obj = frm.save(commit=False)
                    obj.created_by = usuario
                    obj.updated_by = usuario
                    if request.FILES.get('fotografia'):
                        obj.fotografia = move_uploaded_file(
                            request.FILES.get('fotografia'),
                            avanceenflujo_upload_to)
                    if request.FILES.get('fotografia_2'):
                        obj.fotografia_2 = move_uploaded_file(
                            request.FILES.get('fotografia_2'),
                            avanceenflujo_upload_to)
                    if request.FILES.get('fotografia_3'):
                        obj.fotografia_3 = move_uploaded_file(
                            request.FILES.get('fotografia_3'),
                            avanceenflujo_upload_to)
                    if request.FILES.get('fotografia_4'):
                        obj.fotografia_4 = move_uploaded_file(
                            request.FILES.get('fotografia_4'),
                            avanceenflujo_upload_to)
                    if request.FILES.get('fotografia_5'):
                        obj.fotografia_5 = move_uploaded_file(
                            request.FILES.get('fotografia_5'),
                            avanceenflujo_upload_to)
                    obj.save()
                    historia = instanciaflujo.historia.create(
                        accion=accion,
                        extra_data=instanciaflujo.extra_data,
                        created_by=usuario,
                        updated_by=usuario
                    )
                    instanciaflujo.estado_actual = accion.estado_final
                    if (accion.estado_final.es_final is True
                            or accion.estado_final.es_cancelacion is True):
                        instanciaflujo.terminado = True
                    historia.historia_detalle.create(
                        iddocumento_generado=obj.pk,
                        tipo_documento_generado='AvanceEnFlujo',
                        extra_data=historia.extra_data,
                        created_by=usuario,
                        updated_by=usuario,
                    )
                    instanciaflujo.save()
                    rendering = False
                    render_to = 'servicio_index',
                    render_params = {}
    if rendering is True:
        return render(request, render_to, render_params)
    return HttpResponseRedirect(reverse(
        render_to[0], kwargs=render_params))


@valida_acceso(['vehiculo.servicios_vehiculo'])
def index(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    instancias_servicios = list(InstanciaFlujo.objects.filter(
        tipo_instancia="Vehiculo",
        flujo__name='temporal_operaciones').order_by(
            'terminado', '-created_at'))
    search_value = ""
    data = []
    for iserv in instancias_servicios:
        extra_data = json.loads(iserv.extra_data)
        pagado = False
        for h in iserv.historia.all():
            if "pagar" == h.accion.name:
                pagado = True
                break
        data.append({
            'vehiculo': Vehiculo.objects.get(pk=extra_data['idobjeto']),
            'instancia': iserv,
            'pagado': pagado,
        })
    if "POST" == request.method:
        if "search" == request.POST.get('action'):
            search_value = hipernormalize(request.POST.get('valor'))
            data = [reg
                    for reg in data if (
                        search_value in hipernormalize(reg['vehiculo'])
                        or search_value
                        in hipernormalize(reg['vehiculo'].propietario)
                        or search_value
                        in hipernormalize(reg['instancia'].estado_actual)
                    )
                    ]
    toolbar = []
    toolbar.append({'type': 'search'})
    return render(
        request,
        'app/servicios/index.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Servicios',
            'data': data,
            'toolbar': toolbar,
            'search_value': search_value,
            })


@valida_acceso([
    'vehiculo.servicios_vehiculo', 'permiso.mis_servicios_permiso'])
def see(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    toolbar = []
    if not InstanciaFlujo.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    instanciaflujo = InstanciaFlujo.objects.get(pk=pk)
    extra_data = json.loads(instanciaflujo.extra_data)
    vehiculo = Vehiculo.objects.get(pk=extra_data['idobjeto'])
    cliente = vehiculo.propietario
    avanceenflujo = {}
    for h in instanciaflujo.historia.all():
        for d in h.historia_detalle.all():
            if "AvanceEnFlujo" == d.tipo_documento_generado:
                aef = AvanceEnFlujo.objects.get(pk=d.iddocumento_generado)
                avanceenflujo[d.iddocumento_generado] = {
                    'pk': aef.pk,
                    'nota': aef.nota,
                    'fotografia': "{}".format(aef.fotografia).replace(
                        '\\', '/'),
                    'fotografia_2': "{}".format(aef.fotografia_2).replace(
                        '\\', '/'),
                    'fotografia_3': "{}".format(aef.fotografia_3).replace(
                        '\\', '/'),
                    'fotografia_4': "{}".format(aef.fotografia_4).replace(
                        '\\', '/'),
                    'fotografia_5': "{}".format(aef.fotografia_5).replace(
                        '\\', '/'),
                    }
    ver_doctoordenreparacion = usuario.has_perm_or_has_perm_child(
        'doctoordenreparacion.'
        'doctoordenreparacion_docto orden reparacion') or \
        usuario.has_perm_or_has_perm_child(
            'doctoordenreparacion.'
            'ver_orden_de_reparacion_docto orden reparacion')
    ver_avancereparacion = usuario.has_perm_or_has_perm_child(
        'avanceenflujo.avanceenflujo_avance en flujo') or \
        usuario.has_perm_or_has_perm_child(
            'avanceenflujo.'
            'ver_avance_en_flujo_avance en flujo')
    actualizar_avancereparacion = usuario.has_perm_or_has_perm_child(
        'avanceenflujo.actualizar_avance_en_flujo_avance en flujo')
    eliminar_avancereparacion = usuario.has_perm_or_has_perm_child(
        'avanceenflujo.eliminar_avance_en_flujo_avance en flujo')
    print(merge_flujo_acciones(instanciaflujo))
    return render(
        request,
        'app/servicios/see.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Servicio',
            'titulo_descripcion': 'Detalle',
            'toolbar': toolbar,
            'vehiculo': vehiculo,
            'cliente': cliente,
            'instanciaflujo': instanciaflujo,
            'flujo_servicio': merge_flujo_acciones(instanciaflujo),
            'avanceenflujo': avanceenflujo,
            'ver_doctoordenreparacion': ver_doctoordenreparacion,
            'ver_avancereparacion': ver_avancereparacion,
            'actualizar_avancereparacion': actualizar_avancereparacion,
            'eliminar_avancereparacion': eliminar_avancereparacion,
        })


@valida_acceso(['vehiculo.eliminar_servicios_vehiculo'])
def delete(request, pk):
    try:
        if not InstanciaFlujo.objects.filter(pk=pk).exists():
            return HttpResponseRedirect(reverse(
                'item_no_encontrado'))
        obj = InstanciaFlujo.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect(reverse(
            'servicio_index'))
    except ProtectedError as ex:
        print(ex)
        return HttpResponseRedirect(reverse(
            'item_con_relaciones'))


@valida_acceso([
    'vehiculo.agregar_servicios_vehiculo',
    'vehiculo.actualizar_servicios_vehiculo'])
def aplicar_accion(request, pkinstanciaflujo, pkaccion):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    instanciaflujo = InstanciaFlujo.objects.get(pk=pkinstanciaflujo)
    accion = Accion.objects.get(pk=pkaccion)
    extra_data = json.loads(instanciaflujo.extra_data)
    vehiculo = Vehiculo.objects.get(pk=extra_data['idobjeto'])
    cliente = vehiculo.propietario
    toolbar = []
    return render(
        request,
        'app/servicios/aplicar_accion.html',
        {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Servicios',
            'titulo_descripcion': 'Actualizar',
            'instanciaflujo': instanciaflujo,
            'accion': accion,
            'vehiculo': vehiculo,
            'cliente': cliente,
            'frm': FrmAvanceEnFlujo(request.POST or None),
            'toolbar': toolbar,
        }
    )


@valida_acceso([
    'avanceenflujo.actualizar_avance_en_flujo_avance en flujo'])
def update_avanceenflujo(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not AvanceEnFlujo.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    obj = AvanceEnFlujo.objects.get(pk=pk)
    frm = FrmAvanceEnFlujo(instance=obj, data=request.POST or None)
    if "POST" == request.method:
        if frm.is_valid():
            obj = frm.save(commit=False)
            obj.updated_by = usuario
            if request.FILES.get('fotografia'):
                obj.fotografia = move_uploaded_file(
                    request.FILES.get('fotografia'),
                    avanceenflujo_upload_to)
            obj.save()
            instanciaflujo = InstanciaHistoriaDetalle.objects.get(
                tipo_documento_generado='AvanceEnFlujo',
                iddocumento_generado=pk).instanciahistoria.instanciaflujo
            return HttpResponseRedirect(reverse(
                'servicio_see', kwargs={'pk': instanciaflujo.pk}))
    return render(request, 'global/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Nota de Avance en Flujo',
        'titulo_descripcion': 'Actualizar',
        'frm': frm,
    })


@valida_acceso(['avanceenflujo.eliminar_avance_en_flujo_avance en flujo'])
def delete_avanceenflujo(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not AvanceEnFlujo.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    try:
        obj = AvanceEnFlujo.objects.get(pk=pk)
        if InstanciaHistoriaDetalle.objects.filter(
                iddocumento_generado=pk,
                tipo_documento_generado="AvanceEnFlujo").exists():
            InstanciaHistoriaDetalle.objects.get(
                iddocumento_generado=pk,
                tipo_documento_generado="AvanceEnFlujo").delete()
        obj.delete()
    except ProtectedError:
        return HttpResponseRedirect(reverse(
            'item_con_relaciones'))
    return HttpResponseRedirect(reverse('servicio_index'))
