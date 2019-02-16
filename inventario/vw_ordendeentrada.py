from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError

from .models import (
    OrdenDeEntrada,
    newIdentificadorForOrdenDeEntrada,
    Pieza,
    Proveedor,
    Piezas_OrdenDeEntrada,
    OrdenDeCompra)
from .forms import (
    FrmOrdenDeEntrada,
    FrmOrdenDeEntradaSee,
    FrmOrdenDeEntradaUpd)
from initsys.models import Usr
from routines.mkitsafe import valida_acceso
from routines.utils import hipernormalize, truncate, requires_jquery_ui


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
    if usuario.has_perm_or_has_perm_child(
            'ordendeentrada.agregar_ordenes_de_entrada_orden de entrada'):
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
                'ver': usuario.has_perm_or_has_perm_child(
                    'pieza.ordenes_de_entrada_pieza'),
                'actualizar': usuario.has_perm_or_has_perm_child(
                    'ordendeentrada.'
                    'actualizar_ordenes_de_entrada_orden de entrada'
                    ),
                'eliminar': usuario.has_perm_or_has_perm_child(
                    'ordendeentrada.'
                    'eliminar_ordenes_de_entrada_orden de entrada'
                    ),
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
            obj.proveedor = obj.orden_de_compra.proveedor
            obj.save()
            for pza in Pieza.objects.all():
                cant = request.POST.get("pza-cant-{}".format(pza.pk))
                costo = request.POST.get("pza-costo-{}".format(pza.pk))
                importe = request.POST.get("pza-importe-{}".format(pza.pk))
                if cant and float(cant) > 0 and costo and importe:
                    Piezas_OrdenDeEntrada.objects.create(
                        pieza=pza,
                        ordendeentrada=obj,
                        cantidad=truncate(cant),
                        costo=float(costo),
                        importe=float(importe),
                        created_by=usuario,
                        updated_by=usuario
                    )
            return HttpResponseRedirect(reverse(
                'ordendeentrada_see', kwargs={'pk': obj.pk}))
    return render(request, 'inventario/ordendeentrada/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Órden de Entrada',
        'titulo_descripcion': 'Nueva',
        'frm': frm,
        'piezas': list(Pieza.objects.all()),
        'proveedores': list(Proveedor.objects.all()),
        'req_ui': requires_jquery_ui(request),
        'ordenesdecompra': list(OrdenDeCompra.objects.filter(orden_de_entrada__isnull = True) )
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
    return render(request, 'inventario/ordendeentrada/see.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Órden de Entrada',
        'titulo_descripcion': obj,
        'read_only': True,
        'frm': frm,
        'toolbar': toolbar,
        'piezas': list(obj.piezas_entradas.all()),
        'obj': obj,
        'req_ui': requires_jquery_ui(request),
        })


@valida_acceso([
    'ordendeentrada.actualizar_ordenes_de_entrada_orden de entrada'])
def update(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not OrdenDeEntrada.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    obj = OrdenDeEntrada.objects.get(pk=pk)
    frm = FrmOrdenDeEntradaUpd(instance=obj, data=request.POST or None)
    if 'POST' == request.method:
        if frm.is_valid():
            obj = frm.save(commit=False)
            obj.updated_by = usuario
            obj.save()
            Piezas_OrdenDeEntrada.objects.filter(ordendeentrada=obj).delete()
            for pza in Pieza.objects.all():
                cant = request.POST.get("pza-cant-{}".format(pza.pk))
                costo = request.POST.get("pza-costo-{}".format(pza.pk))
                importe = request.POST.get("pza-importe-{}".format(pza.pk))
                if cant and float(cant) > 0 and costo and importe:
                    Piezas_OrdenDeEntrada.objects.create(
                        pieza=pza,
                        ordendeentrada=obj,
                        cantidad=truncate(cant),
                        costo=float(costo),
                        importe=float(importe),
                        created_by=usuario,
                        updated_by=usuario
                    )
            return HttpResponseRedirect(reverse(
                'ordendeentrada_see', kwargs={'pk': obj.pk}))
    return render(request, 'inventario/ordendeentrada/form_upd.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Órden de Entrada',
        'titulo_descripcion': obj,
        'frm': frm,
        'req_ui': requires_jquery_ui(request),
        'obj': obj
    })


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
