"""esteauto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from initsys import views, vw_permiso, vw_usuario, vw_perfil, vw_settings
from app import (
    vw_cliente, vw_vehiculo, vw_servicios, vw_doctoordenreparacion)
from inventario import (
    vw_pieza, vw_proveedor, vw_ordendecompra, vw_ordendeentrada)

urlpatterns = [
    # Base urls
    path(
        'admin/',
        admin.site.urls),

    path(
        'elemento-no-encontrado/',
        views.item_not_found,
        name="item_no_encontrado"),
    path(
        'elemento-con-relaciones/',
        views.item_with_relations,
        name="item_con_relaciones"),
    path(
        'my-panel/',
        views.panel,
        name="panel"),
    path(
        'logout/',
        views.logout,
        name="logout"),
    path(
        '',
        views.index,
        name="index"),
    path(
        'sql/',
        views.sql,
        name='sql'),

    # Permiso
    path(
        'permiso/actualizar/<pk>/',
        vw_permiso.update,
        name='permiso_update'),
    path(
        'permiso/eliminar/<pk>/',
        vw_permiso.delete,
        name='permiso_delete'),
    path(
        'permiso/nuevo/',
        vw_permiso.new,
        name='permiso_new'),
    path(
        'permiso/<pk>/',
        vw_permiso.see,
        name='permiso_see'),
    path(
        'permisos/',
        vw_permiso.index,
        name='permiso_index'),
    path(
        'permission/',
        vw_permiso.permission_index,
        name="permission_index"),

    # Perfil
    path(
        'perfil/actualizar/<pk>/',
        vw_perfil.update,
        name='perfil_update'),
    path(
        'perfil/eliminar/<pk>/',
        vw_perfil.delete,
        name='perfil_delete'),
    path(
        'perfil/nuevo/',
        vw_perfil.new,
        name='perfil_new'),
    path(
        'perfil/<pk>/',
        vw_perfil.see,
        name='perfil_see'),
    path(
        'perfiles/',
        vw_perfil.index,
        name='perfil_index'),

    # Usuario
    path(
        'usuario/actualizar/<pk>/',
        vw_usuario.update,
        name="usuario_update"),
    path(
        'usuario/eliminar/<pk>/',
        vw_usuario.delete,
        name="usuario_delete"),
    path(
        'usuario/nuevo/',
        vw_usuario.new,
        name="usuario_new"),
    path(
        'usuario/<pk>/',
        vw_usuario.see,
        name="usuario_see"),
    path(
        'usuarios/',
        vw_usuario.index,
        name='usuario_index'),
    path(
        'user/',
        vw_usuario.user_index,
        name="user_index"),

    # Settings
    path(
        'settings/configurar/',
        vw_settings.index_adm,
        name='setting_index'),
    path(
        'settings/actualizar/<pk>/',
        vw_settings.update_adm,
        name="setting_update"),
    path(
        'settings/eliminar/<pk>/',
        vw_settings.delete_adm,
        name="setting_delete"),
    path(
        'settings/nuevo/',
        vw_settings.new_adm,
        name="setting_new"),
    path(
        'settings/<pk>/',
        vw_settings.see_adm,
        name="setting_see"),
    path(
        'settings/',
        vw_settings.index,
        name="setting_value"),

    # Cliente
    path(
        'cliente/actualizar/<pk>',
        vw_cliente.update,
        name="cliente_update"),
    path(
        'cliente/eliminar/<pk>',
        vw_cliente.delete,
        name="cliente_delete"),
    path(
        'cliente/nuevo/',
        vw_cliente.new,
        name="cliente_new"),
    path(
        'cliente/<pk>/',
        vw_cliente.see,
        name="cliente_see"),
    path(
        'clientes/',
        vw_cliente.index,
        name="cliente_index"),
    path(
        'mi-perfil/',
        vw_cliente.profile,
        name="cliente_profile"),
    path(
        'mis-servicios/',
        vw_cliente.services,
        name="servicios_cliente"),

    # Vehiculo
    path(
        'vehiculo/actualizar/<pk>',
        vw_vehiculo.update,
        name="vehiculo_update"),
    path(
        'vehiculo/eliminar/<pk>',
        vw_vehiculo.delete,
        name="vehiculo_delete"),
    path(
        'vehiculo/nuevo/<pkcte>',
        vw_vehiculo.new,
        name="vehiculo_new"),
    path(
        'vehiculo/<pk>/',
        vw_vehiculo.see,
        name="vehiculo_see"),
    path(
        'vehiculos/',
        vw_vehiculo.index,
        name="vehiculo_index"),
    path(
        'mis-vehiculos/',
        vw_vehiculo.my_vehicles,
        name="vehiculos_cliente"),

    # Servicio
    path(
        'servicio/nuevo/en-taller/<pkvehiculo>',
        vw_servicios.new_from_taller,
        name="servicio_new_taller"),
    path(
        'servicio/nuevo/en-direccion-particular/<pkvehiculo>',
        vw_servicios.new_from_dir_particular,
        name="servicio_new_particular"),
    path(
        'servicio/executeaccion/',
        vw_servicios.executeaccion,
        name="servicio_executeaccion"),
    path(
        'servicio/aplicaraccion/<pkinstanciaflujo>/<pkaccion>/',
        vw_servicios.aplicar_accion,
        name="servicio_aplicar_accion"),
    path(
        'servicios/eliminar/<pk>/',
        vw_servicios.delete,
        name="servicio_eliminar"),
    path(
        'servicio/<pk>/',
        vw_servicios.see,
        name="servicio_see"),
    path(
        'servicios/',
        vw_servicios.index,
        name="servicio_index"),
    path(
        'servicios/avance/actualizar/<pk>/',
        vw_servicios.update_avanceenflujo,
        name="servicio_avanceenflujo_update"),
    path(
        'servicios/avance/eliminar/<pk>/',
        vw_servicios.delete_avanceenflujo,
        name="servicio_avanceenflujo_delete"),

    # DoctoOrdenReparacion
    path(
        'orden-de-reparacion/<pk>/',
        vw_doctoordenreparacion.see,
        name="doctoordenreparacion_see"),
    path(
        'orden-de-reparacion/actualizar/<pk>/',
        vw_doctoordenreparacion.update,
        name="doctoordenreparacion_update"),
    path(
        'orden-de-reparacion/eliminar/<pk>/',
        vw_doctoordenreparacion.delete,
        name="doctoordenreparacion_delete"),

    # Piezas
    path(
        'refaccion/actualizar/<pk>/',
        vw_pieza.update,
        name='pieza_update'),
    path(
        'refaccion/eliminar/<pk>/',
        vw_pieza.delete,
        name='pieza_delete'),
    path(
        'refaccion/nuevo/',
        vw_pieza.new,
        name='pieza_new'),
    path(
        'refaccion/<pk>/',
        vw_pieza.see,
        name='pieza_see'),
    path(
        'refacciones/',
        vw_pieza.index,
        name='pieza_index'),

    # Proveedores
    path(
        'proveedor/actualizar/<pk>/',
        vw_proveedor.update,
        name='proveedor_update'),
    path(
        'proveedor/eliminar/<pk>/',
        vw_proveedor.delete,
        name='proveedor_delete'),
    path(
        'proveedor/nuevo/',
        vw_proveedor.new,
        name='proveedor_new'),
    path(
        'proveedor/<pk>/',
        vw_proveedor.see,
        name='proveedor_see'),
    path(
        'proveedores/',
        vw_proveedor.index,
        name='proveedor_index'),

    # Órdenes de Compra
    path(
        'orden-de-compra/actualizar/<pk>/',
        vw_ordendecompra.update,
        name='ordendecompra_update'),
    path(
        'orden-de-compra/eliminar/<pk>/',
        vw_ordendecompra.delete,
        name='ordendecompra_delete'),
    path(
        'orden-de-compra/nueva/',
        vw_ordendecompra.new,
        name='ordendecompra_new'),
    path(
        'orden-de-compra/<pk>/',
        vw_ordendecompra.see,
        name='ordendecompra_see'),
    path(
        'ordenes-de-compra/',
        vw_ordendecompra.index,
        name='ordendecompra_index'),

    # Órdenes de Entrada
    path(
        'orden-de-entrada/actualizar/<pk>/',
        vw_ordendeentrada.update,
        name='ordendeentrada_update'),
    path(
        'orden-de-entrada/eliminar/<pk>/',
        vw_ordendeentrada.delete,
        name='ordendeentrada_delete'),
    path(
        'orden-de-entrada/nueva/',
        vw_ordendeentrada.new,
        name='ordendeentrada_new'),
    path(
        'orden-de-entrada/<pk>/',
        vw_ordendeentrada.see,
        name='ordendeentrada_see'),
    path(
        'ordenes-de-entrada/',
        vw_ordendeentrada.index,
        name='ordendeentrada_index'),

]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
