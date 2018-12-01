from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError

from .models import OrdenDeEntrada, newIdentificadorForOrdenDeEntrada, Pieza
from .forms import FrmOrdenDeEntrada, FrmOrdenDeEntradaSee
from initsys.models import Usr
from routines.mkitsafe import valida_acceso
from routines.utils import hipernormalize


@valida_acceso(['pieza.ordenes_de_entrada_pieza'])
def index(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    search_value = ""
    data = list(OrdenDeEntrada.objects.all())
    if "search" == request.POST.get('action'):
        search_value = hipernormalize(request.POST.get('valor'))
        data = [reg
                for reg in data if(
                    search_value in hipernormalize(reg.proveedor)
                )
                ]
    toolbar = []
    if usuario.has_perm_or_has_perm_child('ordendeentrada.agregar_ordenes_de_entrada_orden de entrada'):
        toolbar.append({
            'type': 'link',
            'view': 'ordendeentrada_new',
            'label': '<i class="far fa-file"></i> Nuevo'
        })
    toolbar.append({'type': 'search'})
    return render(
        request,
        'inventario/ordendeentrada/index.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Órdenes de Entrada',
            'data': data,
            'toolbar': toolbar,
            'search_value': search_value,
            'permiso': {
                'ver': usuario.has_perm_or_has_perm_child('ordendeentrada.ordenes_de_entrada_pieza'),
                'actualizar': usuario.has_perm_or_has_perm_child('ordendeentrada.actualizar_ordenes_de_entrada_orden de entrada'),
                'eliminar': usuario.has_perm_or_has_perm_child('ordendeentrada.eliminar_ordenes_de_entrada_orden de entrada'),
            }
            })


@valida_acceso([
    'ordendeentrada.agregar_ordenes_de_entrada_orden de entrada'])
def new(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    frm = FrmOrdenDeEntrada(request.POST or None)
    if 'POST' == request.method:
        if frm.is_valid():
            obj = frm.save(commit=False)
            obj.identificador = newIdentificadorForOrdenDeEntrada()
            obj.created_by = usuario
            obj.updated_by = usuario
            obj.save()
        return HttpResponseRedirect(reverse(
            'ordendeentrada_see', kwargs={'pk': obj.pk}))
    return render(request, 'inventario/ordendecompra/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Órden de Entrada',
        'titulo_descripcion': 'Nueva',
        'frm': frm,
        'piezas': list(Pieza.objects.all()),
    })


@valida_acceso(['pieza.ordenes_de_entrada_pieza'])
def see(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not OrdenDeEntrada.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    obj = OrdenDeEntrada.objects.get(pk=pk)
    frm = FrmOrdenDeEntradaSee(instance=obj)
    toolbar = []
    if usuario.has_perm_or_has_perm_child('pieza.ordenes_de_entrada_pieza'):
        toolbar.append({
            'type': 'link',
            'view': 'ordendeentrada_index',
            'label': '<i class="fas fa-list-ul"></i> Ver todas'})
    if usuario.has_perm_or_has_perm_child(
            'ordendeentrada.actualizar_ordenes_de_entrada_orden de entrada'):
        toolbar.append({
            'type': 'link_pk',
            'view': 'ordendeentrada_update',
            'label': '<i class="far fa-edit"></i> Actualizar',
            'pk': pk})
    if usuario.has_perm_or_has_perm_child(
            'ordendeentrada.eliminar_ordenes_de_entrada_orden de entrada'):
        toolbar.append({
            'type': 'link_pk',
            'view': 'ordendeentrada_delete',
            'label': '<i class="far fa-trash-alt"></i> Eliminar',
            'pk': pk})
    return render(request, 'inventario/ordendecompra/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Órden de Entrada',
        'titulo_descripcion': obj,
        'read_only': True,
        'frm': frm,
        'toolbar': toolbar,
        })

@valida_acceso([
    'ordendeentrada.actualizar_ordenes_de_entrada_orden de entrada'])
def update(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not OrdenDeEntrada.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))


@valida_acceso([
    'ordendeentrada.eliminar_ordenes_de_entrada_orden de entrada'])
def delete(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not OrdenDeEntrada.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    try:
        OrdenDeEntrada.objects.get(pk=pk).delete()
    except ProtectedError:
        return HttpResponseRedirect(reverse(
            'item_con_relaciones'))
    return HttpResponseRedirect(reverse('ordendeentrada_index'))
