from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError

from .models import Pieza, Proveedor, Proveedor_Piezas
from .forms import FrmPieza
from initsys.models import Usr
from routines.mkitsafe import valida_acceso
from routines.utils import hipernormalize


@valida_acceso(['pieza.refacciones_pieza'])
def index(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    search_value = ""
    data = list(Pieza.objects.all())
    if "search" == request.POST.get('action'):
        search_value = hipernormalize(request.POST.get('valor'))
        data = [reg
                for reg in data if(
                    search_value in hipernormalize(reg.nombre)
                    or search_value in hipernormalize(reg.marca)
                    or search_value in hipernormalize(reg.modelo)
                )
                ]
    toolbar = []
    if usuario.has_perm_or_has_perm_child('pieza.agregar_refacciones_pieza'):
        toolbar.append({
            'type': 'link',
            'view': 'pieza_new',
            'label': '<i class="far fa-file"></i> Nuevo'
        })
    toolbar.append({'type': 'search'})
    return render(
        request,
        'inventario/pieza/index.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Refacciones',
            'data': data,
            'toolbar': toolbar,
            'search_value': search_value,
            })


@valida_acceso(['pieza.agregar_refacciones_pieza'])
def new(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    frm = FrmPieza(request.POST or None)
    if 'POST' == request.method:
        if frm.is_valid():
            obj = frm.save(commit=False)
            obj.created_by = usuario
            obj.updated_by = usuario
            obj.save()
            for p in request.POST.getlist('provs'):
                Proveedor_Piezas.objects.create(
                    pieza=obj,
                    proveedor=Proveedor.objects.get(pk=p),
                    created_by=usuario,
                    updated_by=usuario
                )
        return HttpResponseRedirect(reverse(
            'pieza_see', kwargs={'pk': obj.pk}))
    return render(request, 'inventario/pieza/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Refacción',
        'titulo_descripcion': 'Nueva',
        'frm': frm,
        'proveedores': list(Proveedor.objects.all()),
        'proveedores_que_surten': list(),
    })


@valida_acceso(['pieza.refacciones_pieza'])
def see(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Pieza.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    obj = Pieza.objects.get(pk=pk)
    frm = FrmPieza(instance=obj)
    toolbar = []
    if usuario.has_perm_or_has_perm_child('pieza.refacciones_pieza'):
        toolbar.append({
            'type': 'link',
            'view': 'pieza_index',
            'label': '<i class="fas fa-list-ul"></i> Ver todas'})
    if usuario.has_perm_or_has_perm_child(
            'pieza.actualizar_refacciones_pieza'):
        toolbar.append({
            'type': 'link_pk',
            'view': 'pieza_update',
            'label': '<i class="far fa-edit"></i> Actualizar',
            'pk': pk})
    if usuario.has_perm_or_has_perm_child(
            'pieza.eliminar_refacciones_pieza'):
        toolbar.append({
            'type': 'link_pk',
            'view': 'pieza_delete',
            'label': '<i class="far fa-trash-alt"></i> Eliminar',
            'pk': pk})
    return render(request, 'inventario/pieza/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Refacción',
        'titulo_descripcion': obj,
        'read_only': True,
        'frm': frm,
        'toolbar': toolbar,
        'proveedores': list(obj.proveedores.all()),
        'proveedores_que_surten': list(obj.proveedores.all()),
        })


@valida_acceso(['pieza.actualizar_refacciones_pieza'])
def update(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Pieza.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    obj = Pieza.objects.get(pk=pk)
    frm = FrmPieza(instance=obj, data=request.POST or None)
    if 'POST' == request.method:
        if frm.is_valid():
            obj = frm.save(commit=False)
            obj.updated_by = usuario
            obj.save()
            Proveedor_Piezas.objects.filter(pieza=obj).delete()
            for p in request.POST.getlist('provs'):
                Proveedor_Piezas.objects.create(
                    pieza=obj,
                    proveedor=Proveedor.objects.get(pk=p),
                    created_by=usuario,
                    updated_by=usuario
                )
            return HttpResponseRedirect(reverse(
                'pieza_see', kwargs={'pk': obj.pk}))
    return render(request, 'inventario/pieza/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Refacción',
        'titulo_descripcion': obj,
        'frm': frm,
        'proveedores': list(Proveedor.objects.all()),
        'proveedores_que_surten': list(obj.proveedores.all()),
    })


@valida_acceso(['pieza.eliminar_refacciones_pieza'])
def delete(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Pieza.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    try:
        obj = Pieza.objects.get(pk=pk)
        Proveedor_Piezas.objects.filter(pieza=obj).delete()
        obj.delete()
    except ProtectedError:
        return HttpResponseRedirect(reverse(
            'item_con_relaciones'))
    return HttpResponseRedirect(reverse('pieza_index'))
