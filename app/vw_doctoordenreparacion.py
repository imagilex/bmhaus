from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError

from routines.mkitsafe import valida_acceso
from routines.utils import move_uploaded_file
from .models import DoctoOrdenReparacion, doctoordenreparacion_upload_to
from flujo.models import InstanciaHistoriaDetalle
from .forms import (
    FrmDoctoOrdenReparacion,
    FrmDoctoOrdenReparacionGenerales01,
    FrmDoctoOrdenReparacionGenerales02,
    FrmDoctoOrdenReparacionExteriores,
    FrmDoctoOrdenReparacionInteriores,
    FrmDoctoOrdenReparacionAccesorios,
    FrmDoctoOrdenReparacionComponentesMecanicos,
    FrmDoctoOrdenReparacionFirmas
)
from initsys.models import Usr


@valida_acceso()
def see(request,pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not DoctoOrdenReparacion.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    toolbar = []
    obj = DoctoOrdenReparacion.objects.get(pk=pk)
    vehiculo = obj.vehiculo
    historiadetalle = InstanciaHistoriaDetalle.objects.get(iddocumento_generado=pk,tipo_documento_generado='DoctoOrdenReparacion')
    instanciahistoria = historiadetalle.instanciahistoria
    direccion = ""
    if 'Recibir' in instanciahistoria.accion.nombre and 'Taller' in instanciahistoria.accion.nombre:
        direccion = "Av. División del Norte 3259-A<br />La Candelaria, Coyoacán<br />04380, CDMX"
    else:
        direccion_oficina = vehiculo.propietario.direccion_oficina
        direccion = direccion_oficina.asDireccion
    if usuario.has_perm_or_has_perm_child('doctoordenreparacion.actualizar_orden_de_reparacion_docto orden reparacion'):
        toolbar.append({
            'type': 'link_pk',
            'view': 'doctoordenreparacion_update',
            'label': '<i class="far fa-edit"></i> Actualizar',
            'pk': pk})
    if usuario.has_perm_or_has_perm_child('doctoordenreparacion.eliminar_orden_de_reparacion_docto orden reparacion'):
        toolbar.append({
            'type': 'link_pk',
            'view': 'doctoordenreparacion_delete',
            'label': '<i class="far fa-trash-alt"></i> Eliminar',
            'pk': pk})
    return render(
        request,
        'app/doctoordenreparacion/see.html',
        {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Orden de Reparación',
            'titulo_descripcion': "{}/{}".format(vehiculo.propietario, vehiculo),
            'toolbar': toolbar,
            'titulo_frm_1': '',
            'frm1': FrmDoctoOrdenReparacionGenerales01(instance=obj),
            'titulo_frm_2': '',
            'frm2': FrmDoctoOrdenReparacionGenerales02(instance=obj),
            'titulo_frm_3': 'Exteriores',
            'frm3': FrmDoctoOrdenReparacionExteriores(instance=obj),
            'titulo_frm_4': 'Interiores',
            'frm4': FrmDoctoOrdenReparacionInteriores(instance=obj),
            'titulo_frm_5': 'Accesorios',
            'frm5': FrmDoctoOrdenReparacionAccesorios(instance=obj),
            'titulo_frm_6': 'Componentes Mecánicos',
            'frm6': FrmDoctoOrdenReparacionComponentesMecanicos(instance=obj),
            'titulo_frm_7': '',
            'frm7': FrmDoctoOrdenReparacionFirmas(instance=obj),
            'obj': obj,
            'read_only': True,
            'direccion': direccion,
            'vehiculo': vehiculo,
            'propietario': vehiculo.propietario,
        }
    )

@valida_acceso(['doctoordenreparacion.actualizar_orden_de_reparacion_docto orden reparacion'])
def update(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not DoctoOrdenReparacion.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    obj = DoctoOrdenReparacion.objects.get(pk=pk)
    vehiculo = obj.vehiculo
    if "POST" == request.method:
        frm = FrmDoctoOrdenReparacion(instance=obj, data=request.POST)
        if frm.is_valid():
            obj=frm.save(commit=False)
            obj.updated_by = usuario
            if request.FILES.get('fotografia_kilometros'):
                obj.fotografia_kilometros = move_uploaded_file(
                    request.FILES.get('fotografia_kilometros'), 
                    doctoordenreparacion_upload_to)
            if request.FILES.get('fotografia_tanque_de_gasolina'):
                obj.fotografia_tanque_de_gasolina = move_uploaded_file(
                    request.FILES.get('fotografia_tanque_de_gasolina'), 
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
                obj.fotografia_lateral_izquierdo = move_uploaded_file(
                    request.FILES.get('fotografia_lateral_izquierdo'), 
                    doctoordenreparacion_upload_to)
            if request.FILES.get('fotografia_lateral_derecho'):
                obj.fotografia_lateral_derecho = move_uploaded_file(
                    request.FILES.get('fotografia_lateral_derecho'), 
                    doctoordenreparacion_upload_to)
            if request.FILES.get('firma_del_prestador_del_servicio'):
                obj.firma_del_prestador_del_servicio = move_uploaded_file(
                    request.FILES.get('firma_del_prestador_del_servicio'), 
                    doctoordenreparacion_upload_to)
            if request.FILES.get('firma_del_consumidor'):
                obj.firma_del_consumidor = move_uploaded_file(
                    request.FILES.get('firma_del_consumidor'), 
                    doctoordenreparacion_upload_to)
            obj.save()
            return HttpResponseRedirect(reverse('doctoordenreparacion_see', kwargs={'pk': obj.pk}))
    return render(
        request,
        'app/doctoordenreparacion/form.html',
        {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Orden de Reparación',
            'titulo_descripcion': "{}/{}".format(vehiculo.propietario, vehiculo),
            'titulo_frm_1': '',
            'frm1': FrmDoctoOrdenReparacionGenerales01(instance=obj),
            'titulo_frm_2': '',
            'frm2': FrmDoctoOrdenReparacionGenerales02(instance=obj),
            'titulo_frm_3': 'Exteriores',
            'frm3': FrmDoctoOrdenReparacionExteriores(instance=obj),
            'titulo_frm_4': 'Interiores',
            'frm4': FrmDoctoOrdenReparacionInteriores(instance=obj),
            'titulo_frm_5': 'Accesorios',
            'frm5': FrmDoctoOrdenReparacionAccesorios(instance=obj),
            'titulo_frm_6': 'Componentes Mecánicos',
            'frm6': FrmDoctoOrdenReparacionComponentesMecanicos(instance=obj),
            'titulo_frm_7': '',
            'frm7': FrmDoctoOrdenReparacionFirmas(instance=obj),
        }
    )

@valida_acceso(['doctoordenreparacion.eliminar_orden_de_reparacion_docto orden reparacion'])
def delete(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not DoctoOrdenReparacion.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    try:
        obj = DoctoOrdenReparacion.objects.get(pk=pk)
        if InstanciaHistoriaDetalle.objects.filter(iddocumento_generado=pk, tipo_documento_generado="DoctoOrdenReparacion").exists():
            InstanciaHistoriaDetalle.objects.get(iddocumento_generado=pk, tipo_documento_generado="DoctoOrdenReparacion").delete()
        obj.delete()
    except ProtectedError:
        return HttpResponseRedirect(reverse(
            'item_con_relaciones'))
    return HttpResponseRedirect(reverse('servicio_index'))