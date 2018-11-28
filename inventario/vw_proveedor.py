from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError

from .models import Proveedor
from .forms import FrmProveedor
from initsys.models import Direccion, Usr
from initsys.forms import FrmDireccion
from routines.mkitsafe import valida_acceso
from routines.utils import hipernormalize


@valida_acceso(['proveedor.proveedores_proveedor'])
def index(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]


@valida_acceso(['proveedor.agregar_proveedores_proveedor'])
def new(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]


@valida_acceso(['proveedor.proveedores_proveedor'])
def see(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Proveedor.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))


@valida_acceso(['proveedor.actualizar_proveedores_proveedor'])
def update(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Proveedor.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))


@valida_acceso(['proveedor.eliminar_proveedores_proveedor'])
def delete(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Proveedor.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    try:
        Proveedor.objects.get(pk=pk).delete()
    except ProtectedError:
        return HttpResponseRedirect(reverse(
            'item_con_relaciones'))
    return HttpResponseRedirect(reverse('proveedor_index'))
