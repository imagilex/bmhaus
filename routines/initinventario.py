from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group

from initsys.models import Permiso
from .utils import clean_name


def init_inventario_db():
    # Perfiles
    gpo_sadmin = Group.objects.get(name="Super-Administrador")
    gpo_admin = Group.objects.get(name="Administrador")
    gpos = [gpo_admin, gpo_sadmin]

    # Permisos
    if Permiso.objects.filter(nombre='Inventario').exists():
        Permiso.objects.filter(nombre='Inventario')[0].delete()

    p_inv = Permiso.create(
        'Inventario', 'inventario', 'pieza', 7, groups=gpos)

    p_ref = Permiso.create(
        'Refacciones', 'inventario', 'pieza', 1,
        vista="pieza_index", permiso_padre=p_inv, groups=gpos)
    Permiso.create(
        'Agregar Refacciones', 'inventario', 'pieza', 1,
        es_operacion=True, permiso_padre=p_ref, groups=gpos)
    Permiso.create(
        'Actualizar Refacciones', 'inventario', 'pieza', 2,
        es_operacion=True, permiso_padre=p_ref, groups=gpos)
    Permiso.create(
        'Eliminar Refacciones', 'inventario', 'pieza', 3,
        es_operacion=True, permiso_padre=p_ref, groups=gpos)

    p_prov = Permiso.create(
        'Proveedores', 'inventario', 'proveedor', 2,
        vista='proveedor_index', permiso_padre=p_inv, groups=gpos)
    Permiso.create(
        'Agregar Proveedores', 'inventario', 'proveedor', 1,
        es_operacion=True, permiso_padre=p_prov, groups=gpos)
    Permiso.create(
        'Actualizar Proveedores', 'inventario', 'proveedor', 2,
        es_operacion=True, permiso_padre=p_prov, groups=gpos)
    Permiso.create(
        'Eliminar Proveedores', 'inventario', 'proveedor', 3,
        es_operacion=True, permiso_padre=p_prov, groups=gpos)

    p_oc = Permiso.create(
        'Órdenes de Compra en Proveedor', 'inventario',
        'ordendecompra', 4, es_operacion=True, permiso_padre=p_prov,
        groups=gpos)
    Permiso.create(
        'Actualizar Órdenes de Compra en Proveedor', 'inventario',
        'ordendecompra', 1, es_operacion=True, permiso_padre=p_oc,
        groups=gpos)
    Permiso.create(
        'Eliminar Órdenes de Compra en Proveedor', 'inventario',
        'ordendecompra', 2, es_operacion=True, permiso_padre=p_oc,
        groups=gpos)

    p_oe = Permiso.create(
        'Órdenes de Entrada en Proveedor', 'inventario',
        'ordendeentrada', 5, es_operacion=True, permiso_padre=p_prov,
        groups=gpos)
    Permiso.create(
        'Actualizar Órdenes de Entrada en Proveedor', 'inventario',
        'ordendeentrada', 1, es_operacion=True, permiso_padre=p_oe,
        groups=gpos)
    Permiso.create(
        'Eliminar Órdenes de Entrada en Proveedor', 'inventario',
        'ordendeentrada', 2, es_operacion=True, permiso_padre=p_oe,
        groups=gpos)

    p_oc = Permiso.create(
        'Órdenes de Compra', 'inventario', 'pieza', 3,
        vista='ordendecompra_index', permiso_padre=p_inv, groups=gpos)
    Permiso.create(
        'Agregar Órdenes de Compra', 'inventario', 'ordendecompra', 1,
        es_operacion=True, permiso_padre=p_oc, groups=gpos)
    Permiso.create(
        'Actualizar Órdenes de Compra', 'inventario', 'ordendecompra', 2,
        es_operacion=True, permiso_padre=p_oc, groups=gpos)
    Permiso.create(
        'Eliminar Órdenes de Compra', 'inventario', 'ordendecompra', 3,
        es_operacion=True, permiso_padre=p_oc, groups=gpos)

    p_oe = Permiso.create(
        'Órdenes de Entrada', 'inventario', 'pieza', 4,
        vista='ordendeentrada_index', permiso_padre=p_inv, groups=gpos)
    Permiso.create(
        'Agregar Órdenes de Entrada', 'inventario', 'ordendeentrada', 1,
        es_operacion=True, permiso_padre=p_oe, groups=gpos)
    Permiso.create(
        'Actualizar Órdenes de Entrada', 'inventario', 'ordendeentrada', 2,
        es_operacion=True, permiso_padre=p_oe, groups=gpos)
    Permiso.create(
        'Eliminar Órdenes de Entrada', 'inventario', 'ordendeentrada', 3,
        es_operacion=True, permiso_padre=p_oe, groups=gpos)
