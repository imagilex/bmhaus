from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError

from .models import OrdenDeEntrada
from .forms import FrmOrdenDeEntrada
from initsys.models import Usr
from routines.mkitsafe import valida_acceso
from routines.utils import hipernormalize


@valida_acceso(['ordendeentrada.ordenes_de_entrada_orden de entrada'])
def index(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]


@valida_acceso([
    'ordendeentrada.agregar_ordenes_de_entrada_orden de entrada'])
def new(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]


@valida_acceso(['ordendeentrada.ordenes_de_entrada_orden de entrada'])
def see(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not OrdenDeEntrada.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))


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
