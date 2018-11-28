from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError

from .models import OrdenDeCompra
from .forms import FrmOrdenDeCompra
from initsys.models import Usr
from routines.mkitsafe import valida_acceso
from routines.utils import hipernormalize


@valida_acceso(['ordendecompra.ordenes_de_compra_orden de compra'])
def index(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]


@valida_acceso(['ordendecompra.agregar_ordenes_de_compra_orden de compra'])
def new(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]


@valida_acceso(['ordendecompra.ordenes_de_compra_orden de compra'])
def see(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not OrdenDeCompra.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))


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
