from django.db import models
from django.utils import timezone

from datetime import datetime, date

from initsys.models import Usr, Direccion
from cfdi.models import OpcionCatalogoSAT

# Create your models here.

vehiculo_upload_to = 'vehiculos'
doctoordenreparacion_upload_to = 'doctoordenreparacion'
avanceenflujo_upload_to = 'avanceenflujo'


def newIdentificadorForDoctoOrdenReparacion():
    today = datetime.now()
    res = "OR-" + today.strftime("%y%m") + "-"
    res += "{:03d}".format(DoctoOrdenReparacion.objects.filter(
        identificador__startswith=res).count() + 1)
    return res


def getTime():
    return datetime.time(datetime.now())


class Cliente(Usr):
    idcliente = models.AutoField(primary_key=True)
    apellido_materno = models.CharField(
        max_length=25,
        null=True, blank=True)
    telefono_oficina = models.CharField(
        max_length=10,
        null=True, blank=True)
    extension = models.CharField(max_length=5, null=True, blank=True)
    direccion_casa = models.ForeignKey(
        Direccion, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="cliente_casas")
    direccion_oficina = models.ForeignKey(
        Direccion, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="cliente_oficina")
    razon_social = models.CharField(max_length=254, null=True, blank=True)
    rfc = models.CharField(max_length=13, null=True, blank=True)
    formapago = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="cliente_formapago",
        limit_choices_to={'catalogo__idsat': 'FormaPago'})
    moneda = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="cliente_moneda",
        limit_choices_to={'catalogo__idsat': 'Moneda'})
    metodopago = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="cliente_metodopago",
        limit_choices_to={'catalogo__idsat': 'MetodoPago'})
    residenciafiscal = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="cliente_residenciafiscal",
        limit_choices_to={'catalogo__idsat': 'Pais'})
    usocfdi = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="cliente_usocfdi",
        limit_choices_to={'catalogo__idsat': 'UsoCFDi'})
    claveprodserv = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="cliente_claveprodserv",
        limit_choices_to={'catalogo__idsat': 'ClaveProdServ'})
    claveunidad = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="cliente_claveunidad",
        limit_choices_to={'catalogo__idsat': 'ClaveUnidad'})
    impuesto = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="cliente_impuesto",
        limit_choices_to={'catalogo__idsat': 'Impuesto'})
    tipofactor = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="cliente_tipofactor",
        limit_choices_to={'catalogo__idsat': 'TipoFactor'})

    class Meta:
        ordering = ['first_name', 'last_name', 'apellido_materno']

    def __str__(self):
        return "{} {}".format(
            self.get_full_name(), self.apellido_materno or '').strip()

    def __unicode__(self):
        return self.__str__()


class Vehiculo(models.Model):
    idvehiculo = models.AutoField(primary_key=True)
    propietario = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="vehiculos")
    marca = models.CharField(max_length=20)
    serie = models.CharField(max_length=20, null=True, blank=True)
    modelo = models.CharField(max_length=20)
    año = models.PositiveSmallIntegerField(default=2016)
    clase = models.CharField(max_length=20, null=True, blank=True)
    tipo = models.CharField(max_length=20, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    vin = models.CharField(max_length=17, null=True, blank=True)
    numero_de_placa = models.CharField(max_length=10)
    fotografia = models.ImageField(
        null=True, blank=True, upload_to=vehiculo_upload_to)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['marca', 'serie', 'tipo', 'numero_de_placa']

    def __str__(self):
        return "{} {}".format(
            self.marca or '', self.tipo or '').strip()

    def __unicode__(self):
        return self.__str__()


class DoctoOrdenReparacion(models.Model):
    estado_tanque_gasolina_0 = '0'
    estado_tanque_gasolina_1_4 = '1_4'
    estado_tanque_gasolina_1_2 = '1_2'
    estado_tanque_gasolina_3_4 = '3_4'
    estado_tanque_gasolina_4_4 = '4_4'
    estado_tanque_gasolina = (
        (estado_tanque_gasolina_0, '0'),
        (estado_tanque_gasolina_1_4, '1/4'),
        (estado_tanque_gasolina_1_2, '1/2'),
        (estado_tanque_gasolina_3_4, '3/4'),
        (estado_tanque_gasolina_4_4, '4/4'),
    )
    iddoctoordenreparacion = models.AutoField(primary_key=True)
    identificador = models.CharField(max_length=50, blank=True)
    vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.PROTECT,
        related_name="ordenesreparacion")
    kilometros = models.IntegerField(blank=True, default=0)
    tanque_de_gasolina = models.CharField(
        max_length=20,
        choices=estado_tanque_gasolina,
        default=estado_tanque_gasolina_0)
    fotografia_kilometros = models.ImageField(
        blank=True, upload_to=doctoordenreparacion_upload_to)
    fotografia_tanque_de_gasolina = models.ImageField(
        blank=True, upload_to=doctoordenreparacion_upload_to)
    fotografia_superior = models.ImageField(
        blank=True, upload_to=doctoordenreparacion_upload_to)
    fotografia_frente = models.ImageField(
        blank=True, upload_to=doctoordenreparacion_upload_to)
    fotografia_trasera = models.ImageField(
        blank=True, upload_to=doctoordenreparacion_upload_to)
    fotografia_lateral_izquierdo = models.ImageField(
        blank=True, upload_to=doctoordenreparacion_upload_to)
    fotografia_lateral_derecho = models.ImageField(
        blank=True, upload_to=doctoordenreparacion_upload_to)
    fecha_de_recepcion = models.DateField(default=date.today)
    hora_de_recepcion = models.TimeField(default=getTime)
    servicio_solicitado = models.TextField(blank=True)
    unidad_de_luces = models.BooleanField(default=False)
    cuartos = models.BooleanField(default=False)
    antena = models.BooleanField(default=False)
    espejo_lateral = models.BooleanField(default=False)
    cristales = models.BooleanField(default=False)
    emblema = models.BooleanField(default=False)
    llantas = models.BooleanField(default=False)
    tapon_de_ruedas = models.BooleanField(default=False)
    molduras_completas = models.BooleanField(default=False)
    tapon_de_gasolina = models.BooleanField(default=False)
    carroceria_sin_golpes = models.BooleanField(default=False)
    bocinas_de_claxon = models.BooleanField(default=False)
    limpiadores = models.BooleanField(default=False)
    instrumentos_de_tablero = models.BooleanField(default=False)
    calefaccion = models.BooleanField(default=False)
    radio = models.BooleanField(default=False)
    bocinas = models.BooleanField(default=False)
    encendedor = models.BooleanField(default=False)
    espejo_retrovisor = models.BooleanField(default=False)
    ceniceros = models.BooleanField(default=False)
    cinturones = models.BooleanField(default=False)
    botones_de_interiores = models.BooleanField(default=False)
    manijas_de_interiores = models.BooleanField(default=False)
    tapetes = models.BooleanField(default=False)
    vestiduras = models.BooleanField(default=False)
    gato = models.BooleanField(default=False)
    maneral_de_gato = models.BooleanField(default=False)
    llave_de_ruedas = models.BooleanField(default=False)
    estuche_de_herramientas = models.BooleanField(default=False)
    triangulo_de_seguridad = models.BooleanField(default=False)
    llanta_de_refaccion = models.BooleanField(default=False)
    extingidor = models.BooleanField(default=False)
    claxon = models.BooleanField(default=False)
    tapon_de_aceite = models.BooleanField(default=False)
    tapon_de_radiador = models.BooleanField(default=False)
    varilla_de_aceite = models.BooleanField(default=False)
    filtro_de_aire = models.BooleanField(default=False)
    bateria = models.BooleanField(default=False)
    costo_de_revision = models.DecimalField(
        max_digits=13, decimal_places=2, default=1000.00)
    observaciones = models.TextField(blank=True)
    firma_del_prestador_del_servicio = models.ImageField(
        blank=True, upload_to=doctoordenreparacion_upload_to)
    firma_del_consumidor = models.ImageField(
        blank=True, upload_to=doctoordenreparacion_upload_to)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_de_recepcion', '-hora_de_recepcion']

    def __str__(self):
        return "{} ({})".format(
            self.vehiculo, self.fecha_y_hora_de_recepcion)

    def __unicode__(self):
        return self.__str__()


class AvanceEnFlujo(models.Model):
    idavanceenflujo = models.AutoField(primary_key=True)
    nota = models.TextField(null=True, blank=True)
    fotografia = models.ImageField(
        blank=True, upload_to=avanceenflujo_upload_to)
    fotografia_2 = models.ImageField(
        blank=True, upload_to=avanceenflujo_upload_to)
    fotografia_3 = models.ImageField(
        blank=True, upload_to=avanceenflujo_upload_to)
    fotografia_4 = models.ImageField(
        blank=True, upload_to=avanceenflujo_upload_to)
    fotografia_5 = models.ImageField(
        blank=True, upload_to=avanceenflujo_upload_to)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = []

    def __str__(self):
        return "{}".format(self.nota)

    def __unicode__(self):
        return self.__str__()
