from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError

from .models import (
    OrdenDeCompra,
    newIdentificadorForOrdenDeCompra,
    Pieza,
    Piezas_OrdenDeCompra)
from .forms import FrmOrdenDeCompra, FrmOrdenDeCompraSee
from initsys.models import Usr
from routines.mkitsafe import valida_acceso
from routines.utils import hipernormalize


@valida_acceso(['pieza.ordenes_de_compra_pieza'])
def index(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    search_value = ""
    data = list(OrdenDeCompra.objects.all())
    if "search" == request.POST.get('action'):
        search_value = hipernormalize(request.POST.get('valor'))
        data = [reg
                for reg in data if(
                    search_value in hipernormalize(reg.proveedor)
                )
                ]
    toolbar = []
    if usuario.has_perm_or_has_perm_child('ordendecompra.agregar_ordenes_de_compra_orden de compra'):
        toolbar.append({
            'type': 'link',
            'view': 'ordendecompra_new',
            'label': '<i class="far fa-file"></i> Nuevo'
        })
    toolbar.append({'type': 'search'})
    return render(
        request,
        'inventario/ordendecompra/index.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Órdenes de Compra',
            'data': data,
            'toolbar': toolbar,
            'search_value': search_value,
            'permiso': {
                'ver': usuario.has_perm_or_has_perm_child('pieza.ordenes_de_compra_pieza'),
                'actualizar': usuario.has_perm_or_has_perm_child('ordendecompra.actualizar_ordenes_de_compra_orden de compra'),
                'eliminar': usuario.has_perm_or_has_perm_child('ordendecompra.eliminar_ordenes_de_compra_orden de compra'),
            }
            })


@valida_acceso(['ordendecompra.agregar_ordenes_de_compra_orden de compra'])
def new(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    frm = FrmOrdenDeCompra(request.POST or None)
    if 'POST' == request.method:
        if frm.is_valid():
            obj = frm.save(commit=False)
            obj.identificador = newIdentificadorForOrdenDeCompra()
            obj.created_by = usuario
            obj.updated_by = usuario
            obj.save()
            for pza in Pieza.objects.all():
                cant = request.POST.get("pza-cant-{}".format(pza.pk))
                if cant:
                    Piezas_OrdenDeCompra.objects.create(
                        pieza=pza,
                        ordendecompra=obj,
                        cantidad=int(cant),
                        created_by=usuario,
                        updated_by=usuario
                    )
        return HttpResponseRedirect(reverse(
            'ordendecompra_see', kwargs={'pk': obj.pk}))
    return render(request, 'inventario/ordendecompra/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Órden de Compra',
        'titulo_descripcion': 'Nueva',
        'frm': frm,
        'piezas': list(Pieza.objects.all()),
    })


@valida_acceso(['pieza.ordenes_de_compra_pieza'])
def see(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not OrdenDeCompra.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    obj = OrdenDeCompra.objects.get(pk=pk)
    frm = FrmOrdenDeCompraSee(instance=obj)
    toolbar = []
    if usuario.has_perm_or_has_perm_child('pieza.ordenes_de_compra_pieza'):
        toolbar.append({
            'type': 'link',
            'view': 'ordendecompra_index',
            'label': '<i class="fas fa-list-ul"></i> Ver todas'})
    if usuario.has_perm_or_has_perm_child(
            'ordendecompra.actualizar_ordenes_de_compra_orden de compra'):
        toolbar.append({
            'type': 'link_pk',
            'view': 'ordendecompra_update',
            'label': '<i class="far fa-edit"></i> Actualizar',
            'pk': pk})
    if usuario.has_perm_or_has_perm_child(
            'ordendecompra.eliminar_ordenes_de_compra_orden de compra'):
        toolbar.append({
            'type': 'link_pk',
            'view': 'ordendecompra_delete',
            'label': '<i class="far fa-trash-alt"></i> Eliminar',
            'pk': pk})
    print(obj.piezas.all())
    return render(request, 'inventario/ordendecompra/see.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Órden de Compra',
        'titulo_descripcion': obj,
        'read_only': True,
        'frm': frm,
        'toolbar': toolbar,
        'piezas': list(obj.piezas_requeridas.all()),
        })


@valida_acceso(['ordendecompra.actualizar_ordenes_de_compra_orden de compra'])
def update(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not OrdenDeCompra.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))


@valida_acceso(['ordendecompra.eliminar_ordenes_de_compra_orden de compra'])
def delete(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not OrdenDeCompra.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    try:
        OrdenDeCompra.objects.get(pk=pk).delete()
    except ProtectedError:
        return HttpResponseRedirect(reverse(
            'item_con_relaciones'))
    return HttpResponseRedirect(reverse('ordendecompra_index'))
