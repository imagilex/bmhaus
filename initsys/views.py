from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.staticfiles import finders
from django.conf import settings

from random import shuffle
import os

from .forms import AccUsr
from .models import Usr
from routines.mkitsafe import valida_acceso

# Create your views here.


def index(request):
    frm = AccUsr(request.POST or None)
    if(frm.is_valid() and 'POST' == request.method):
        user = frm.login(request)
        if user is not None and user.is_active:
            auth.login(request, user)
            usuario = Usr.objects.get(id=user.pk)
            request.session['usuario'] = usuario.pk
            request.session['usuario_pic'] = "{}".format(usuario.fotografia)
            return HttpResponseRedirect(reverse('panel'))
    auth.logout(request)
    bg_imgs = []
    bgdir_imgs = []
    donotdeletebg = finders.find('background/donotdelete.imgx')
    if donotdeletebg is not None:
        bgdir = os.path.join(os.path.dirname(donotdeletebg), 'bg')
        bgstartdir = os.path.join(os.path.dirname(donotdeletebg), 'start')
        bgdir_imgs = [
            'background/bg/'+f
            for f in os.listdir(bgdir)
            if os.path.isfile(os.path.join(bgdir, f))]
        bgstartdir_imgs = [
            'background/start/'+f
            for f in os.listdir(bgstartdir)
            if os.path.isfile(os.path.join(bgstartdir, f))]
        shuffle(bgdir_imgs)
        shuffle(bgstartdir_imgs)
        bg_imgs = bgdir_imgs[:5]
    return render(request, 'index.html', {
        'bg_start': True,
        'bg_imgs': bg_imgs,
        'bg_serv': bgdir_imgs,
        'bg_serv_no': len(bgdir_imgs),
        'footer': True})


def logout(request):
    return HttpResponseRedirect(reverse('index'))


@valida_acceso()
def item_not_found(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    return render(
        request,
        'item_no_encontrado.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Elemento no encontrado'
        }
    )


@valida_acceso()
def item_with_relations(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    return render(
        request,
        'item_con_relaciones.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Elemento relacionado'})


@valida_acceso()
def panel(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    return render(
        request,
        'my_panel.html', {
            'menu_main': usuario.main_menu_struct(),
            # 'footer': True,
            'usuario': usuario.first_name
        })
