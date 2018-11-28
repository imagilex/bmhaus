from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError

from .models import Cliente, Vehiculo, vehiculo_upload_to
from .forms import FrmVehiculo
from initsys.models import Usr
from flujo.models import InstanciaFlujo
from routines.mkitsafe import valida_acceso
from routines.utils import move_uploaded_file, hipernormalize


@valida_acceso(['vehiculo.vehiculos_vehiculo'])
def index(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    search_value = ""
    data = list(Vehiculo.objects.all().order_by(
        'propietario', 'marca', 'serie', 'modelo', 'numero_de_placa'))
    if "POST" == request.method:
        if "search" == request.POST.get('action'):
            search_value = hipernormalize(request.POST.get('valor'))
            data = [reg
                    for reg in data if (
                        search_value in hipernormalize(reg.propietario)
                        or search_value in hipernormalize(reg.marca)
                        or search_value in hipernormalize(reg.serie)
                        or search_value in hipernormalize(reg.modelo)
                        or search_value in hipernormalize(reg.año)
                        or search_value in hipernormalize(reg.clase)
                        or search_value in hipernormalize(reg.tipo)
                        or search_value in hipernormalize(reg.color)
                        or search_value in hipernormalize(reg.vin)
                        or search_value in hipernormalize(reg.numero_de_placa))
                    ]
    toolbar = []
    toolbar.append({'type': 'search'})
    return render(
        request,
        'app/vehiculo/index.html',
        {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Vehiculos',
            'vehiculos': data,
            'toolbar': toolbar,
            'search_value': search_value,
        }
    )


@valida_acceso(['vehiculo.agregar_vehiculos_vehiculo'])
def new(request, pkcte):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    cte = Cliente.objects.get(pk=pkcte)
    if 'POST' == request.method:
        frm = FrmVehiculo(data=request.POST or None)
        if frm.is_valid():
            obj = frm.save(commit=False)
            obj.propietario = cte
            obj.created_by = usuario
            obj.updated_by = usuario
            if request.FILES.get('fotografia'):
                obj.fotografia = move_uploaded_file(
                    request.FILES.get('fotografia'), vehiculo_upload_to)
            obj.save()
            return HttpResponseRedirect(reverse(
                'vehiculo_see', kwargs={'pk': obj.pk}
            ))
    frm = FrmVehiculo(data=request.POST or None)
    return render(request, 'global/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Vehiculos',
        'titulo_descripcion': 'Nuevo ({})'.format(cte),
        'frm': frm
    })


@valida_acceso([
    'vehiculo.vehiculos_vehiculo', 'vehiculo.mi_vehiculo_vehiculo'])
def see(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Vehiculo.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    obj = Vehiculo.objects.get(pk=pk)
    frm = FrmVehiculo(instance=obj)
    toolbar = []
    if usuario.has_perm_or_has_perm_child('cliente.clientes_user'):
        toolbar.append({
            'type': 'link_pk',
            'view': 'cliente_see',
            'pk': obj.propietario.pk,
            'label': '<i class="fas fa-user"></i> Ver Cliente'})
    if usuario.has_perm_or_has_perm_child(
            'vehiculo.actualizar_vehiculos_vehiculo'):
        toolbar.append({
            'type': 'link_pk',
            'view': 'vehiculo_update',
            'label': '<i class="far fa-edit"></i> Actualizar',
            'pk': pk})
    if usuario.has_perm_or_has_perm_child(
            'vehiculo.eliminar_vehiculos_vehiculo'):
        toolbar.append({
            'type': 'link_pk',
            'view': 'vehiculo_update',
            'label': '<i class="far fa-trash-alt"></i> Eliminar',
            'pk': pk})
    ids = '{"idobjeto":' + pk + '}'
    instancias_servicios = list(InstanciaFlujo.objects.filter(
        tipo_instancia="Vehiculo",
        flujo__name='temporal_operaciones', extra_data=ids).order_by(
            'terminado', '-created_at'))
    data = []
    for iserv in instancias_servicios:
        pagado = False
        for h in iserv.historia.all():
            if "pagar" == h.accion.name:
                pagado = True
                break
        data.append({
            'vehiculo': obj,
            'instancia': iserv,
            'pagado': pagado,
        })
    return render(request, 'app/vehiculo/see.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': obj,
        'read_only': True,
        'frm': frm,
        'fotografia': obj.fotografia,
        'toolbar': toolbar,
        'data': data,
        })


@valida_acceso(['vehiculo.actualizar_vehiculos_vehiculo'])
def update(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Vehiculo.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    obj = Vehiculo.objects.get(pk=pk)
    if 'POST' == request.method:
        frm = FrmVehiculo(instance=obj, data=request.POST)
        if frm.is_valid():
            obj = frm.save(commit=False)
            obj.updated_by = usuario
            if request.FILES.get('fotografia'):
                obj.fotografia = move_uploaded_file(
                    request.FILES.get('fotografia'), vehiculo_upload_to)
            obj.save()
            return HttpResponseRedirect(reverse(
                'vehiculo_see', kwargs={'pk': obj.pk}
            ))
    frm = FrmVehiculo(instance=obj)
    return render(request, 'global/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Vehiculos',
        'titulo_descripcion': '{} ({})'.format(obj, obj.propietario),
        'frm': frm
    })


@valida_acceso(['vehiculo.eliminar_vehiculos_vehiculo'])
def delete(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    try:
        if not Vehiculo.objects.filter(pk=pk).exists():
            return HttpResponseRedirect(reverse(
                'item_no_encontrado'))
        obj = Vehiculo.objects.get(pk=pk)
        ctepk = obj.propietario.pk
        obj.delete()
        return HttpResponseRedirect(reverse(
            'cliente_see', kwargs={'pk': ctepk}))
    except ProtectedError:
        return HttpResponseRedirect(reverse(
            'item_con_relaciones'))


@valida_acceso(['vehiculo.mis_autos_vehiculo'])
def my_vehicles(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Cliente.objects.filter(idusuario=usuario.pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    cte = Cliente.objects.get(idusuario=usuario.pk)
    return render(request, 'app/vehiculo/mis_vehiculos.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Mis Autos',
        'vehiculos': [{
            'pk': v.pk,
            'name': "{}".format(v),
            'fotografia': "{}".format(v.fotografia).replace('\\', '/')
            } for v in list(cte.vehiculos.all())],
    })
