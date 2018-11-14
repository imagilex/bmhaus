from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.staticfiles import finders
from django.conf import settings

from random import shuffle
import os
import json

from .forms import AccUsr
from .models import Usr
from app.models import Cliente, AvanceEnFlujo
from flujo.models import InstanciaFlujo
from routines.mkitsafe import valida_acceso
from routines.utils import is_mobile

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
        'footer': True,
        'is_mobile': is_mobile(request)})


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
    data = []
    if Cliente.objects.filter(idusuario=usuario.pk).exists():
        cte = Cliente.objects.get(idusuario=usuario.pk)
        ids = []
        for v in list(cte.vehiculos.all()):
            ids.append('{"idobjeto":' + str(v.pk) + '}')
        instancias_servicios = InstanciaFlujo.objects.filter(
            tipo_instancia="Vehiculo",
            flujo__name='temporal_operaciones',
            extra_data__in=ids,
            terminado=False).order_by(
                'terminado', '-created_at')
        if instancias_servicios.exists():
            iserv = instancias_servicios[0]
            extra_data = json.loads(iserv.extra_data)
            pagado = False
            for h in iserv.historia.all():
                if "pagar" == h.accion.name:
                    pagado = True
                    break
            avanceenflujo = {}
            for h in iserv.historia.all():
                for d in h.historia_detalle.all():
                    if "AvanceEnFlujo" == d.tipo_documento_generado:
                        aef = AvanceEnFlujo.objects.get(
                            pk=d.iddocumento_generado)
                        avanceenflujo[d.iddocumento_generado] = {
                            'pk': aef.pk,
                            'nota': aef.nota,
                            'fotografia': "{}".format(
                                aef.fotografia).replace('\\', '/')}
            data = {
                'vehiculo': cte.vehiculos.get(pk=extra_data['idobjeto']),
                'instanciaflujo': iserv,
                'pagado': pagado,
                'avanceenflujo': avanceenflujo,
            }
    ver_doctoordenreparacion = usuario.has_perm_or_has_perm_child(
        'doctoordenreparacion.'
        'doctoordenreparacion_docto orden reparacion') \
        or usuario.has_perm_or_has_perm_child('doctoordenreparacion.'
        'ver_orden_de_reparacion_docto orden reparacion')
    ver_avancereparacion = usuario.has_perm_or_has_perm_child(
        'avanceenflujo.avanceenflujo_avance en flujo') \
        or usuario.has_perm_or_has_perm_child(
            'avanceenflujo.ver_avance_en_flujo_avance en flujo')
    return render(
        request,
        'my_panel.html', {
            'menu_main': usuario.main_menu_struct(),
            # 'footer': True,
            'usuario': usuario.first_name,
            'data': data,
            'ver_doctoordenreparacion': ver_doctoordenreparacion,
            'ver_avancereparacion': ver_avancereparacion,
        })
