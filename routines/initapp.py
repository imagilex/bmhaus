from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group

from initsys.models import Permiso, Usr
from app.models import Cliente
from cfdi.models import CatalogoSAT, OpcionCatalogoSAT
from flujo.models import Flujo, Estado, Accion
from .utils import clean_name


def init_app_db():
    # Perfiles
    gpos = ["Super-Administrador", "Administrador"]
    gpo_cte = Group.objects.create(name="Cliente")

    # Permisos
    p_cte = Permiso.create(
        "Clientes", "app", "cliente", 1, vista="cliente_index",
        groups=gpos)
    Permiso.create(
        "Agregar Clientes", "app", "cliente", 1, groups=gpos,
        es_operacion=True, permiso_padre=p_cte)
    Permiso.create(
        "Actualizar Clientes", "app", "cliente", 2, groups=gpos,
        es_operacion=True, permiso_padre=p_cte)
    Permiso.create(
        "Eliminar Clientes", "app", "cliente", 3, groups=gpos,
        es_operacion=True, permiso_padre=p_cte)
    p_veh = Permiso.create(
        "Vehiculos", "app", "vehiculo", 4, groups=gpos, es_operacion=True,
        permiso_padre=p_cte)
    Permiso.create(
        "Agregar Vehiculos", "app", "vehiculo", 1, groups=gpos,
        es_operacion=True, permiso_padre=p_veh)
    Permiso.create(
        "Actualizar Vehiculos", "app", "vehiculo", 2, groups=gpos,
        es_operacion=True, permiso_padre=p_veh)
    Permiso.create(
        "Eliminar Vehiculos", "app", "vehiculo", 3, groups=gpos,
        es_operacion=True, permiso_padre=p_veh)
    Permiso.create(
        "Mi Perfil", 'app', 'cliente', 2, vista="cliente_profile",
        groups=[gpo_cte])
    Permiso.create(
        "Mis Autos", 'app', 'vehiculo', 3, vista="vehiculos_cliente",
        groups=[gpo_cte])
    Permiso.create(
        "Mis Servicios", 'app', 'cliente', 4, vista="servicios_cliente",
        groups=[gpo_cte])

    # Usuario
    pwd_cte = "bmhaus-cte"
    usr_cte = Cliente.objects.create(
        username='cliente', first_name='Cliente',
        is_staff=False, is_active=True, is_superuser=False,
        usuario='cliente', contraseña=pwd_cte)
    usr_cte.set_password(pwd_cte)
    print("Usuario Creado:\n\t   Usuario: {}\n\tContrasena: {}\n".format(
        usr_cte.username, pwd_cte))
    usr_cte.groups.set([gpo_cte])
    usr_cte.save()


def init_app_predata():
    c_formapago, aux = CatalogoSAT.objects.get_or_create(
        idsat="FormaPago", nombre="SAT Forma de Pago")
    c_moneda, aux = CatalogoSAT.objects.get_or_create(
        idsat="Moneda", nombre="SAT Moneda")
    c_metodopago, aux = CatalogoSAT.objects.get_or_create(
        idsat="MetodoPago", nombre="SAT Método de Pago")
    c_pais, aux = CatalogoSAT.objects.get_or_create(
        idsat="Pais", nombre="SAT País")
    c_usocfdi, aux = CatalogoSAT.objects.get_or_create(
        idsat="UsoCFDi", nombre="SAT Uso del CFDi")
    c_claveprodserv, aux = CatalogoSAT.objects.get_or_create(
        idsat="ClaveProdServ", nombre="SAT Clave del Producto o Servicio")
    c_claveunidad, aux = CatalogoSAT.objects.get_or_create(
        idsat="ClaveUnidad", nombre="SAT Clave de la Unidad")
    c_impuesto, aux = CatalogoSAT.objects.get_or_create(
        idsat="Impuesto", nombre="SAT Impuesto")
    c_tipofactor, aux = CatalogoSAT.objects.get_or_create(
        idsat="TipoFactor", nombre="SAT Tipo de Factor")

    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="1",
        mostrar_como="1 | Efectivo")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="2",
        mostrar_como="2 | Cheque nominativo")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="3",
        mostrar_como="3 | Transferencia electrónica de fondos")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="4",
        mostrar_como="4 | Tarjeta de crédito")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="5",
        mostrar_como="5 | Monedero electrónico")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="6",
        mostrar_como="6 | Dinero electrónico")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="8",
        mostrar_como="8 | Vales de despensa")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="12",
        mostrar_como="12 | Dación en pago")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="13",
        mostrar_como="13 | Pago por subrogación")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="14",
        mostrar_como="14 | Pago por consignación")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="15",
        mostrar_como="15 | Condonación")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="17",
        mostrar_como="17 | Compensación")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="23",
        mostrar_como="23 | Novación")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="24",
        mostrar_como="24 | Confusión")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="25",
        mostrar_como="25 | Remisión de deuda")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="26",
        mostrar_como="26 | Prescripción o caducidad")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="27",
        mostrar_como="27 | A satisfacción del acreedor")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="28",
        mostrar_como="28 | Tarjeta de débito")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="29",
        mostrar_como="29 | Tarjeta de servicios")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="30",
        mostrar_como="30 | Aplicación de anticipos")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_formapago, clave_sat="99",
        mostrar_como="99 | Por definir")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_moneda, clave_sat="CAD",
        mostrar_como="CAD | Dolar Canadiense")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_moneda, clave_sat="EUR",
        mostrar_como="EUR | Euro")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_moneda, clave_sat="MXN",
        mostrar_como="MXN | Peso Mexicano")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_moneda, clave_sat="USD",
        mostrar_como="USD | Dolar americano")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_metodopago, clave_sat="PUE",
        mostrar_como="PUE | Pago en una sola exhibición")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_metodopago, clave_sat="PPD",
        mostrar_como="PPD | Pago en parcialidades o diferido")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_pais, clave_sat="USA",
        mostrar_como="USA | Estados Unidos (los)")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_pais, clave_sat="MEX",
        mostrar_como="MEX | México")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="G01",
        mostrar_como="G01 | Adquisición de mercancias")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="G02",
        mostrar_como="G02 | Devoluciones, descuentos o bonificaciones")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="G03",
        mostrar_como="G03 | Gastos en general")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="I01",
        mostrar_como="I01 | Construcciones")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="I02",
        mostrar_como="I02 | Mobilario y equipo de oficina por inversiones")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="I03",
        mostrar_como="I03 | Equipo de transporte")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="I04",
        mostrar_como="I04 | Equipo de computo y accesorios")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="I05",
        mostrar_como="I05 | Dados, troqueles, moldes"
        ", matrices y herramental")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="I06",
        mostrar_como="I06 | Comunicaciones telefónicas")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="I07",
        mostrar_como="I07 | Comunicaciones satelitales")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="I08",
        mostrar_como="I08 | Otra maquinaria y equipo")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="D01",
        mostrar_como="D01 | Honorarios médicos, dentales y gas"
        "tos hospitalarios.")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="D02",
        mostrar_como="D02 | Gastos médicos por incapacidad o discapacidad")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="D03",
        mostrar_como="D03 | Gastos funerales.")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="D04",
        mostrar_como="D04 | Donativos.")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="D05",
        mostrar_como="D05 | Intereses reales efectivamente pagados por cr"
        "éditos hipotecarios (casa habitación).")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="D06",
        mostrar_como="D06 | Aportaciones voluntarias al SAR.")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="D07",
        mostrar_como="D07 | Primas por seguros de gastos médicos.")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="D08",
        mostrar_como="D08 | Gastos de transportación escolar obligatoria.")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="D09",
        mostrar_como="D09 | Depósitos en cuentas para el ahorro, primas qu"
        "e tengan como base planes de pensiones.")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="D10",
        mostrar_como="D10 | Pagos por servicios educativos (colegiaturas)")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_usocfdi, clave_sat="P01",
        mostrar_como="P01 | Por definir")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_claveprodserv, clave_sat="01010101",
        mostrar_como="01010101 | No existe en el catálogo")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_claveprodserv, clave_sat="25171718",
        mostrar_como="25171718 | Kits de reparación de frenos")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_claveprodserv, clave_sat="25172511",
        mostrar_como="25172511 | Kit de reparación de llantas")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_claveprodserv, clave_sat="26101412",
        mostrar_como="26101412 | Kit de reparación de motor")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_claveprodserv, clave_sat="26101513",
        mostrar_como="26101513 | Kit de reparación de motores")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_claveprodserv, clave_sat="78181500",
        mostrar_como="78181500 | Servicios de mantenimiento y reparación d"
        "e vehículos")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_claveprodserv, clave_sat="78181507",
        mostrar_como="78181507 | Reparación y mantenimiento automotor y d"
        "e camiones ligeros")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_claveunidad, clave_sat="E48",
        mostrar_como="E48 | Unidad de servicio")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_claveunidad, clave_sat="H87",
        mostrar_como="H87 | Pieza")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_claveunidad, clave_sat="HUR",
        mostrar_como="HUR | Hora")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_claveunidad, clave_sat="LH",
        mostrar_como="LH | Hora de trabajo")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_impuesto, clave_sat="001",
        mostrar_como="001 | ISR")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_impuesto, clave_sat="002",
        mostrar_como="002 | IVA")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_impuesto, clave_sat="003",
        mostrar_como="003 | IEPS")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_tipofactor, clave_sat="Tasa",
        mostrar_como="Tasa | Tasa")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_tipofactor, clave_sat="Cuota",
        mostrar_como="Cuota | Cuota")
    OpcionCatalogoSAT.objects.get_or_create(
        catalogo=c_tipofactor, clave_sat="Exento",
        mostrar_como="Exento | Exento")

    iflujo, aux = Flujo.objects.get_or_create(
        nombre="Temporal Operaciones",
        descripcion="Flujo temporal para servicios")

    e0, aux = Estado.objects.get_or_create(
        no_estado=0, nombre="Inicio", flujo=iflujo, es_inicial=True)
    e1, aux = Estado.objects.get_or_create(
        no_estado=1, nombre="Recibido", flujo=iflujo)
    e2, aux = Estado.objects.get_or_create(
        no_estado=2, nombre="Diagnosticado", flujo=iflujo)
    e3, aux = Estado.objects.get_or_create(
        no_estado=3, nombre="Presupuestado", flujo=iflujo)
    e4, aux = Estado.objects.get_or_create(
        no_estado=4, nombre="Presupuesto Aceptado", flujo=iflujo)
    e5, aux = Estado.objects.get_or_create(
        no_estado=5, nombre="Pendiente de Surtir", flujo=iflujo)
    e6, aux = Estado.objects.get_or_create(
        no_estado=6, nombre="Por Reparar", flujo=iflujo)
    e7, aux = Estado.objects.get_or_create(
        no_estado=7, nombre="Reparado", flujo=iflujo)
    e8, aux = Estado.objects.get_or_create(
        no_estado=8, nombre="Por Entregar", flujo=iflujo)
    e9, aux = Estado.objects.get_or_create(
        no_estado=9, nombre="Entregado", flujo=iflujo, es_final=True)
    e10, aux = Estado.objects.get_or_create(
        no_estado=10, nombre="Cancelado por Rechazo de Presupuesto",
        flujo=iflujo, es_cancelacion=True)

    Accion.objects.get_or_create(
        estado_inicial=e0,
        nombre="Recibir Vehículo en Taller",
        estado_final=e1,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e0,
        nombre="Recibir Vehículo en Domicilio",
        estado_final=e1,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e1,
        nombre="Diagnosticar",
        estado_final=e2,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e2,
        nombre="Presupuestar",
        estado_final=e3,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e3,
        nombre="Pagar",
        estado_final=e3,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e3,
        nombre="Aceptar Presupuesto",
        estado_final=e4,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e3,
        nombre="Rechazar Presupuesto",
        stado_final=e10,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e4,
        nombre="Pagar",
        estado_final=e4,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e4,
        nombre="Generar Orden de Compra",
        estado_final=e5,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e4,
        nombre="Generar Orden de Trabajo",
        estado_final=e6,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e5,
        nombre="Pagar",
        estado_final=e5,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e5,
        nombre="Generar Orden de Trabajo",
        estado_final=e6,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e6,
        nombre="Pagar",
        estado_final=e6,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e6,
        nombre="Vehículo Reparado",
        estado_final=e7,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e7,
        nombre="Pagar",
        estado_final=e7,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e7,
        nombre="Revisión de Calidad Realizada",
        estado_final=e8,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e8,
        nombre="Pagar",
        estado_final=e8,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e8,
        nombre="Facturar",
        estado_final=e8,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e8,
        nombre="Entregar en Taller",
        estado_final=e9,
        flujo=iflujo)
    Accion.objects.get_or_create(
        estado_inicial=e8,
        nombre="Entregar en Domicilio",
        estado_final=e9,
        flujo=iflujo)


def upd_app_db():
    gpo_cte = Group.objects.get(name="Cliente")
    perm_mis_veh = Permiso.objects.get(codename='mis_autos_vehiculo')
    Permiso.create(
        "Mi vehiculo", 'app', 'vehiculo', 1, groups=[gpo_cte],
        es_operacion=True, permiso_padre=perm_mis_veh)


def upd_app_db_20181104():
    gpos = list(Group.objects.filter(name__icontains='Administrador'))
    Permiso.create(
        'Master Vehiculos',
        'app',
        'vehiculo',
        5,
        mostrar_como='Vehiculos',
        vista='vehiculo_index',
        groups=gpos)
    pserv = Permiso.create(
        'Servicios',
        'app',
        'vehiculo',
        6,
        vista='servicio_index',
        groups=gpos)
    Permiso.create(
        'Agregar Servicios',
        'app',
        'vehiculo',
        1,
        es_operacion=True,
        permiso_padre=pserv,
        groups=gpos)
    Permiso.create(
        'Actualizar Servicios',
        'app',
        'vehiculo',
        2,
        es_operacion=True,
        permiso_padre=pserv,
        groups=gpos)
    Permiso.create(
        'Eliminar Servicios',
        'app',
        'vehiculo',
        3,
        es_operacion=True,
        permiso_padre=pserv,
        groups=gpos)

    for obj in Flujo.objects.all():
        obj.name = clean_name(obj.nombre)
        obj.save()
    for obj in Estado.objects.all():
        obj.name = clean_name(obj.nombre)
        obj.save()
    for obj in Accion.objects.all():
        obj.name = clean_name(obj.nombre)
        obj.save()

    pserv = Permiso.objects.get(codename='servicios_vehiculo')
    pdocto_orden_rep = Permiso.create(
        'doctoordenreparacion',
        'app',
        'doctoordenreparacion',
        4,
        mostrar_como='Orden de Reparacion',
        es_operacion=True,
        permiso_padre=pserv,
        groups=gpos)
    Permiso.create(
        'Actualizar Orden de Reparacion',
        'app',
        'doctoordenreparacion',
        2,
        es_operacion=True,
        permiso_padre=pdocto_orden_rep,
        groups=gpos)
    Permiso.create(
        'Eliminar Orden de Reparacion',
        'app',
        'doctoordenreparacion',
        3,
        es_operacion=True,
        permiso_padre=pdocto_orden_rep,
        groups=gpos)
    pavance = Permiso.create(
        'avanceenflujo',
        'app',
        'avanceenflujo',
        5,
        mostrar_como='Avance en Flujo',
        es_operacion=True,
        permiso_padre=pserv,
        groups=gpos)
    Permiso.create(
        'Actualizar Avance en Flujo',
        'app',
        'avanceenflujo',
        2,
        es_operacion=True,
        permiso_padre=pavance,
        groups=gpos)
    Permiso.create(
        'Eliminar Avance en Flujo',
        'app',
        'avanceenflujo',
        3,
        es_operacion=True,
        permiso_padre=pavance,
        groups=gpos)

    gpo_cte = list(Group.objects.filter(name__icontains='Cliente'))
    pmisserv = Permiso.objects.get(codename='mis_servicios_permiso')
    Permiso.create(
        'Ver Orden de Reparacion',
        'app',
        'doctoordenreparacion',
        1,
        es_operacion=True,
        permiso_padre=pmisserv,
        groups=gpo_cte)
    Permiso.create(
        'Ver Avance en Flujo',
        'app',
        'avanceenflujo',
        2,
        es_operacion=True,
        permiso_padre=pmisserv,
        groups=gpo_cte)


def upd_app_db_20181112():
    flujo = Flujo.objects.get(name="temporal_operaciones")
    edo = flujo.estados.get(name="inicio")
    edo.porcentaje = 0
    edo.save()
    edo = flujo.estados.get(name="recibido")
    edo.porcentaje = 10
    edo.save()
    edo = flujo.estados.get(name="diagnosticado")
    edo.porcentaje = 20
    edo.save()
    edo = flujo.estados.get(name="presupuestado")
    edo.porcentaje = 30
    edo.save()
    edo = flujo.estados.get(name="cancelado_por_rechazo_de_presupuesto")
    edo.porcentaje = 100
    edo.save()
    edo = flujo.estados.get(name="presupuesto_aceptado")
    edo.porcentaje = 40
    edo.save()
    edo = flujo.estados.get(name="pendiente_de_surtir")
    edo.porcentaje = 40
    edo.save()
    edo = flujo.estados.get(name="por_reparar")
    edo.porcentaje = 50
    edo.save()
    edo = flujo.estados.get(name="reparado")
    edo.porcentaje = 80
    edo.save()
    edo = flujo.estados.get(name="por_entregar")
    edo.porcentaje = 90
    edo.save()
    edo = flujo.estados.get(name="entregado")
    edo.porcentaje = 100
    edo.save()
