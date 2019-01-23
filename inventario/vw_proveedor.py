from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError

from .models import Proveedor, Pieza, Proveedor_Piezas
from .forms import FrmProveedor
from initsys.models import Direccion, Usr
from initsys.forms import FrmDireccion
from routines.mkitsafe import valida_acceso
from routines.utils import hipernormalize


@valida_acceso(['proveedor.proveedores_proveedor'])
def index(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    search_value = ""
    data = list(Proveedor.objects.all())
    if "search" == request.POST.get('action'):
        search_value = hipernormalize(request.POST.get('valor'))
        data = [reg
                for reg in data if(
                    search_value in hipernormalize(reg.razon_social)
                    or search_value in hipernormalize(reg.nombre)
                    or search_value in hipernormalize(reg.rfc)
                    or search_value in hipernormalize(reg.direccion.estado)
                    or search_value in hipernormalize(reg.direccion.municipio)
                    or search_value in hipernormalize(reg.direccion.colonia)
                )
                ]
    toolbar = []
    if usuario.has_perm_or_has_perm_child(
            'proveedor.agregar_proveedores_proveedor'):
        toolbar.append({
            'type': 'link',
            'view': 'proveedor_new',
            'label': '<i class="far fa-file"></i> Nuevo'
        })
    toolbar.append({'type': 'search'})
    return render(
        request,
        'inventario/proveedor/index.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Proveedores',
            'data': data,
            'toolbar': toolbar,
            'search_value': search_value,
            })


@valida_acceso(['proveedor.agregar_proveedores_proveedor'])
def new(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    frm = FrmProveedor(request.POST or None)
    frmDir = FrmDireccion(request.POST or None)
    if 'POST' == request.method:
        if frm.is_valid() and frmDir.is_valid():
            obj = frm.save(commit=False)
            dir = frmDir.save()
            obj.direccion = dir
            obj.created_by = usuario
            obj.updated_by = usuario
            obj.save()
            for p in request.POST.getlist('pzas'):
                Proveedor_Piezas.objects.create(
                    pieza=Pieza.objects.get(pk=p),
                    proveedor=obj,
                    costo=request.POST.get('costo-' + p),
                    created_by=usuario,
                    updated_by=usuario
                )
        return HttpResponseRedirect(reverse(
            'proveedor_see', kwargs={'pk': obj.pk}))
    return render(request, 'inventario/proveedor/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Proveedor',
        'titulo_descripcion': 'Nuevo',
        'titulo_frm_1': 'Datos Generales',
        'frm': frm,
        'titulo_frm_2': 'Dirección',
        'frm2': frmDir,
        'piezas': list(Pieza.objects.all()),
        'piezas_que_surte': list(),
        'pp_piezas': list()
    })


@valida_acceso(['proveedor.proveedores_proveedor'])
def see(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Proveedor.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    obj = Proveedor.objects.get(pk=pk)
    frm = FrmProveedor(instance=obj)
    frmDir = FrmDireccion(instance=obj.direccion)
    toolbar = []
    if usuario.has_perm_or_has_perm_child('proveedor.proveedores_proveedor'):
        toolbar.append({
            'type': 'link',
            'view': 'proveedor_index',
            'label': '<i class="fas fa-list-ul"></i> Ver todas'})
    if usuario.has_perm_or_has_perm_child(
            'proveedor.actualizar_proveedores_proveedor'):
        toolbar.append({
            'type': 'link_pk',
            'view': 'proveedor_update',
            'label': '<i class="far fa-edit"></i> Actualizar',
            'pk': pk})
    if usuario.has_perm_or_has_perm_child(
            'proveedor.eliminar_proveedores_proveedor'):
        toolbar.append({
            'type': 'link_pk',
            'view': 'proveedor_delete',
            'label': '<i class="far fa-trash-alt"></i> Eliminar',
            'pk': pk})
    return render(request, 'inventario/proveedor/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Proveedor',
        'titulo_descripcion': obj,
        'read_only': True,
        'titulo_frm_1': 'Datos Generales',
        'frm': frm,
        'titulo_frm_2': 'Dirección',
        'frm2': frmDir,
        'toolbar': toolbar,
        'piezas': list(obj.piezas.all()),
        'piezas_que_surte': list(obj.piezas.all()),
        'pp_piezas': list(obj.pp_piezas.all())
        })


@valida_acceso(['proveedor.actualizar_proveedores_proveedor'])
def update(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Proveedor.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    obj = Proveedor.objects.get(pk=pk)
    frm = FrmProveedor(instance=obj, data=request.POST or None)
    frmDir = FrmDireccion(instance=obj.direccion, data=request.POST or None)
    if 'POST' == request.method:
        if frm.is_valid():
            obj = frm.save(commit=False)
            obj.updated_by = usuario
            obj.save()
            Proveedor_Piezas.objects.filter(proveedor=obj).delete()
            for p in request.POST.getlist('pzas'):
                Proveedor_Piezas.objects.create(
                    pieza=Pieza.objects.get(pk=p),
                    proveedor=obj,
                    costo=request.POST.get('costo-' + p),
                    created_by=usuario,
                    updated_by=usuario
                )
            return HttpResponseRedirect(reverse(
                'proveedor_see', kwargs={'pk': obj.pk}))
    return render(request, 'inventario/proveedor/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Proveedor',
        'titulo_descripcion': obj,
        'titulo_frm_1': 'Datos Generales',
        'frm': frm,
        'titulo_frm_2': 'Dirección',
        'frm2': frmDir,
        'piezas': list(Pieza.objects.all()),
        'piezas_que_surte': list(obj.piezas.all()),
        'pp_piezas': list(obj.pp_piezas.all())
    })


@valida_acceso(['proveedor.eliminar_proveedores_proveedor'])
def delete(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Proveedor.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    try:
        obj = Proveedor.objects.get(pk=pk)
        Proveedor_Piezas.objects.filter(proveedor=obj).delete()
        obj.delete()
    except ProtectedError as err:
        return HttpResponseRedirect(reverse(
            'item_con_relaciones'))
    return HttpResponseRedirect(reverse('proveedor_index'))
