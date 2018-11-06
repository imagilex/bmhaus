from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.db.models import ProtectedError

import json

from .models import Cliente
from .forms import (
    FrmCliente, FrmClienteUsr, FrmClienteContacto, FrmClienteFacturacion)
from initsys.models import Usr, usr_upload_to
from initsys.forms import FrmDireccion
from flujo.models import InstanciaFlujo
from routines.mkitsafe import valida_acceso
from routines.utils import move_uploaded_file


@valida_acceso(['cliente.clientes_user'])
def index(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    data = list(Cliente.objects.all())
    toolbar = []
    if usuario.has_perm_or_has_perm_child('cliente.agregar_clientes_user'):
        toolbar.append({
            'type': 'link',
            'view': 'cliente_new',
            'label': '<i class="far fa-file"></i> Nuevo'})
    return render(
        request,
        'app/cliente/index.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Clientes',
            'data': data,
            'toolbar': toolbar
            })


@valida_acceso(['cliente.agregar_clientes_user'])
def new(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if 'POST' == request.method:
        frm = FrmCliente(request.POST)
        if frm.is_valid():
            obj = frm.save(commit=False)
            obj.username = obj.usuario
            obj.set_password(obj.contraseña)
            obj.created_by = usuario
            obj.updated_by = usuario
            if request.FILES.get('fotografia'):
                obj.fotografia = move_uploaded_file(
                    request.FILES.get('fotografia'), usr_upload_to)
            obj.save()
            obj.groups.add(Group.objects.get(name='Cliente'))
            obj.save()
            return HttpResponseRedirect(reverse(
                'cliente_see', kwargs={'pk': obj.pk}
            ))
    frmUsr = FrmClienteUsr(request.POST or None)
    frmContacto = FrmClienteContacto(request.POST or None)
    frmFacturacion = FrmClienteFacturacion(request.POST or None)
    return render(request, 'global/form2.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Clientes',
        'titulo_descripcion': 'Nuevo',
        'titulo_frm_1': 'Usuario',
        'frm': frmUsr,
        'titulo_frm_2': 'Contacto',
        'frm2': frmContacto,
        'titulo_frm_4': 'Facturación',
        'frm4': frmFacturacion,
    })


@valida_acceso(['cliente.clientes_user'])
def see(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Cliente.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    obj = Cliente.objects.get(pk=pk)
    if 'POST' == request.method:
        if 'add-home-add' == request.POST.get('action'):
            frm = FrmDireccion(request.POST)
            dir = frm.save()
            obj.direccion_casa = dir
            obj.direccion_casa.created_by = usuario
            obj.direccion_casa.updated_by = usuario
            obj.save()
        elif 'upd-home-add' == request.POST.get('action'):
            frm = FrmDireccion(
                instance=obj.direccion_casa, data=request.POST)
            obj.direccion_casa.updated_by = usuario
            dir = frm.save()
        elif 'add-office-add' == request.POST.get('action'):
            frm = FrmDireccion(request.POST)
            dir = frm.save()
            obj.direccion_oficina = dir
            obj.direccion_oficina.created_by = usuario
            obj.direccion_oficina.updated_by = usuario
            obj.save()
        elif 'upd-office-add' == request.POST.get('action'):
            frm = FrmDireccion(
                instance=obj.direccion_oficina, data=request.POST)
            obj.direccion_oficina.updated_by = usuario
            dir = frm.save()
    frmUsr = FrmClienteUsr(instance=obj)
    frmContacto = FrmClienteContacto(instance=obj)
    frmFacturacion = FrmClienteFacturacion(instance=obj)
    toolbar = []
    if usuario.has_perm_or_has_perm_child('cliente.clientes_user'):
        toolbar.append({
            'type': 'link',
            'view': 'cliente_index',
            'label': '<i class="fas fa-list-ul"></i> Ver todos'})
    if usuario.has_perm_or_has_perm_child(
            'cliente.actualizar_clientes_user'):
        toolbar.append({
            'type': 'link_pk',
            'view': 'cliente_update',
            'label': '<i class="far fa-edit"></i> Actualizar',
            'pk': pk})
    if usuario.has_perm_or_has_perm_child(
            'cliente.eliminar_clientes_user'):
        toolbar.append({
            'type': 'link_pk',
            'view': 'cliente_delete',
            'label': '<i class="far fa-trash-alt"></i> Eliminar',
            'pk': pk})
    return render(request, 'app/cliente/see.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Cliente',
        'titulo_descripcion': obj,
        'read_only': True,
        'titulo_frm_1': 'Usuario',
        'frm': frmUsr,
        'titulo_frm_2': 'Contacto',
        'frm2': frmContacto,
        'titulo_frm_4': 'Facturación',
        'frm4': frmFacturacion,
        'fotografia': obj.fotografia,
        'toolbar': toolbar,
        'direccion_casa': obj.direccion_casa,
        'direccion_oficina': obj.direccion_oficina,
        'frm_direccion_casa': FrmDireccion(instance=obj.direccion_casa),
        'frm_direccion_oficina': FrmDireccion(
            instance=obj.direccion_oficina),
        'vehiculos': list(obj.vehiculos.all()),
        'cte': obj,
        })


@valida_acceso(['cliente.actualizar_clientes_user'])
def update(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Cliente.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    obj = Cliente.objects.get(pk=pk)
    if 'POST' == request.method:
        frm = FrmCliente(instance=obj, data=request.POST)
        if frm.is_valid():
            obj = frm.save(commit=False)
            obj.username = obj.usuario
            obj.set_password(obj.contraseña)
            obj.created_by = usuario
            obj.updated_by = usuario
            if request.FILES.get('fotografia'):
                obj.fotografia = move_uploaded_file(
                    request.FILES.get('fotografia'), usr_upload_to)
            obj.save()
            obj.groups.add(Group.objects.get(name='Cliente'))
            obj.save()
            return HttpResponseRedirect(reverse(
                'cliente_see', kwargs={'pk': obj.pk}
            ))
    frmUsr = FrmClienteUsr(instance=obj)
    frmContacto = FrmClienteContacto(instance=obj)
    frmFacturacion = FrmClienteFacturacion(instance=obj)
    return render(request, 'global/form2.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Clientes',
        'titulo_descripcion': obj,
        'titulo_frm_1': 'Usuario',
        'frm': frmUsr,
        'titulo_frm_2': 'Contacto',
        'frm2': frmContacto,
        'titulo_frm_4': 'Facturación',
        'frm4': frmFacturacion,
    })


@valida_acceso(['cliente.eliminar_clientes_user'])
def delete(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Cliente.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    try:
        Cliente.objects.get(pk=pk).delete()
    except ProtectedError:
        return HttpResponseRedirect(reverse(
            'item_con_relaciones'))
    return HttpResponseRedirect(reverse('cliente_index'))


@valida_acceso()
def profile(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Cliente.objects.filter(idusuario=usuario.pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    obj = Cliente.objects.get(idusuario=usuario.pk)
    frmUsr = FrmClienteUsr(instance=obj)
    frmContacto = FrmClienteContacto(instance=obj)
    frmFacturacion = FrmClienteFacturacion(instance=obj)
    return render(request, 'app/cliente/see.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': obj,
        'read_only': True,
        'titulo_frm_1': 'Usuario',
        'frm': frmUsr,
        'titulo_frm_2': 'Contacto',
        'frm2': frmContacto,
        'titulo_frm_4': 'Facturación',
        'frm4': frmFacturacion,
        'fotografia': obj.fotografia,
        'direccion_casa': obj.direccion_casa,
        'direccion_oficina': obj.direccion_oficina,
        'frm_direccion_casa': FrmDireccion(instance=obj.direccion_casa),
        'frm_direccion_oficina': FrmDireccion(
            instance=obj.direccion_oficina),
        })


@valida_acceso()
def services(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Cliente.objects.filter(idusuario=usuario.pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    cte = Cliente.objects.get(idusuario=usuario.pk)
    ids = []
    for v in list(cte.vehiculos.all()):
        ids.append('{"idobjeto":' + str(v.pk) + '}')
    instancias_servicios = list(InstanciaFlujo.objects.filter(
        tipo_instancia="Vehiculo",
        flujo__name='temporal_operaciones', extra_data__in=ids).order_by(
            'terminado', '-created_at'))
    data = []
    for iserv in instancias_servicios:
        extra_data = json.loads(iserv.extra_data)
        pagado = False
        for h in iserv.historia.all():
            if "pagar" == h.accion.name:
                pagado = True
                break
        data.append({
            'vehiculo': cte.vehiculos.get(pk=extra_data['idobjeto']),
            'instancia': iserv,
            'pagado': pagado,
        })
    toolbar = []
    return render(
        request,
        'app/servicios/index_cte.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Servicios',
            'data': data,
            'toolbar': toolbar
            })
