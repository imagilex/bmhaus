from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError

from .models import Pieza
from .forms import FrmPieza
from initsys.models import Usr
from routines.mkitsafe import valida_acceso
from routines.utils import hipernormalize


@valida_acceso(['pieza.refacciones_pieza'])
def index(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]


@valida_acceso(['pieza.agregar_refacciones_pieza'])
def new(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]


@valida_acceso(['pieza.refacciones_pieza'])
def see(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Pieza.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))


@valida_acceso(['pieza.actualizar_refacciones_pieza'])
def update(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Pieza.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))


@valida_acceso(['pieza.eliminar_refacciones_pieza'])
def delete(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not Pieza.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse(
            'item_no_encontrado'))
    try:
        Pieza.objects.get(pk=pk).delete()
    except ProtectedError:
        return HttpResponseRedirect(reverse(
            'item_con_relaciones'))
    return HttpResponseRedirect(reverse('pieza_index'))
