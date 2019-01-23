from django.db import models

from datetime import datetime, date
from decimal import Decimal

from initsys.models import Usr, Direccion
from cfdi.models import OpcionCatalogoSAT

banco_BANAMEX = 'BANAMEX'
banco_BANCOMEXT = 'BANCOMEXT'
banco_BANOBRAS = 'BANOBRAS'
banco_BBVABANCOMER = 'BBVA BANCOMER'
banco_SANTANDER = 'SANTANDER'
banco_BANJERCITO = 'BANJERCITO'
banco_HSBC = 'HSBC'
banco_GEMONEY = 'GE MONEY'
banco_BAJIO = 'BAJÍO'
banco_IXE = 'IXE'
banco_INBURSA = 'INBURSA'
banco_INTERACCIONES = 'INTERACCIONES'
banco_MIFEL = 'MIFEL'
banco_SCOTIABANK = 'SCOTIABANK'
banco_BANREGIO = 'BANREGIO'
banco_INVEX = 'INVEX'
banco_BANSI = 'BANSI'
banco_AFIRME = 'AFIRME'
banco_BANORTE = 'BANORTE'
banco_ABNAMRO = 'ABNAMRO'
banco_AMERICANEXPRESS = 'AMERICAN EXPRESS'
banco_BAMSA = 'BAMSA'
banco_TOKYO = 'TOKYO'
banco_JPMORGAN = 'JP MORGAN'
banco_BMONEX = 'BMONEX'
banco_VEPORMAS = 'VE POR MAS'
banco_ING = 'ING'
banco_DEUTSCHE = 'DEUTSCHE'
banco_CREDITSUISSE = 'CREDIT SUISSE'
banco_AZTECA = 'AZTECA'
banco_AUTOFIN = 'AUTOFIN'
banco_BARCLAYS = 'BARCLAYS'
banco_COMPARTAMOS = 'COMPARTAMOS'
banco_FAMSA = 'FAMSA'
banco_BMULTIVA = 'BMULTIVA'
banco_PRUDENTIAL = 'PRUDENTIAL'
banco_WALMART = 'WAL-MART'
banco_NAFIN = 'NAFIN'
banco_REGIONAL = 'REGIONAL'
banco_BANCOPPEL = 'BANCOPPEL'
banco_ABCCAPITAL = 'ABC CAPITAL'
banco_UBSBANK = 'UBS BANK'
banco_FACIL = 'FÁCIL'
banco_VOLKSWAGEN = 'VOLKSWAGEN'
banco_CIBanco = 'CIBanco'
banco_BBASE = 'BBASE'
banco_BANKAOOL = 'BANKAOOL'
banco_PagaTodo = 'PagaTodo'
banco_BIM = 'BIM'
banco_SABADELL = 'SABADELL'
banco_BANSEFI = 'BANSEFI'
banco_HIPOTECARIAFEDERAL = 'HIPOTECARIA FEDERAL'
banco_MONEXCB = 'MONEXCB'
banco_GBM = 'GBM'
banco_MASARICB = 'MASARI CB'
banco_INBURSA = 'C.B. INBURSA'
banco_VALUE = 'VALUÉ'
banco_CBBASE = 'CB BASE'
banco_TIBER = 'TIBER'
banco_VECTOR = 'VECTOR'
banco_BB = 'B&B'
banco_INTERCAM = 'INTERCAM'
banco_MULTIVA = 'MULTIVA'
banco_ACCIVAL = 'ACCIVAL'
banco_MERRILLLYNCH = 'MERRILL LYNCH'
banco_FINAMEX = 'FINAMEX'
banco_VALMEX = 'VALMEX'
banco_UNICA = 'ÚNICA'
banco_ASEGURADORAMAPFRE = 'ASEGURADORA MAPFRE'
banco_AFOREPROFUTURO = 'AFORE PROFUTURO'
banco_CBACTINBER = 'CB ACTINBER'
banco_ACTINVESI = 'ACTINVE SI'
banco_SKANDIA = 'SKANDIA'
banco_CONSULTORÍA = 'CONSULTORÍA'
banco_CBDEUTSCHE = 'CBDEUTSCHE'
banco_ZURICH = 'ZURICH'
banco_ZURICHVI = 'ZURICHVI'
banco_HIPOTECARIASUCASITA = 'HIPOTECARIA SU CASITA'
banco_INTERCAM = 'C.B. INTERCAM'
banco_VANGUARDIA = 'C.B. VANGUARDIA'
banco_BULLTICKCB = 'BULLTICK C.B.'
banco_STERLING = 'STERLING'
banco_FINCOMUN = 'FINCOMUN'
banco_HDISEGUROS = 'HDI SEGUROS'
banco_ORDER = 'ORDER'
banco_AKALA = 'AKALA'
banco_JPMORGANCB = 'JP MORGAN C.B.'
banco_REFORMA = 'REFORMA'
banco_STP = 'STP'
banco_TELECOMM = 'TELECOMM'
banco_EVERCORE = 'EVERCORE'
banco_SKANDIA = 'SKANDIA'
banco_SEGMTY = 'SEGMTY'
banco_ASEA = 'ASEA'
banco_KUSPIT = 'KUSPIT'
banco_SOFIEXPRESS = 'SOFIEXPRESS'
banco_UNAGRA = 'UNAGRA'
banco_OPCIONESEMPRESARIALESDELNOROESTE = 'OPCIONES EMPRESARIALES DEL NOROESTE'
banco_LIBERTAD = 'LIBERTAD'
banco_CLS = 'CLS'
banco_INDEVAL = 'INDEVAL'
banco_N_A = 'N/A'

bancos = (
    (banco_ABCCAPITAL, banco_ABCCAPITAL),
    (banco_ABNAMRO, banco_ABNAMRO),
    (banco_ACCIVAL, banco_ACCIVAL),
    (banco_ACTINVESI, banco_ACTINVESI),
    (banco_AFIRME, banco_AFIRME),
    (banco_AFOREPROFUTURO, banco_AFOREPROFUTURO),
    (banco_AKALA, banco_AKALA),
    (banco_AMERICANEXPRESS, banco_AMERICANEXPRESS),
    (banco_ASEA, banco_ASEA),
    (banco_ASEGURADORAMAPFRE, banco_ASEGURADORAMAPFRE),
    (banco_AUTOFIN, banco_AUTOFIN),
    (banco_AZTECA, banco_AZTECA),
    (banco_BB, banco_BB),
    (banco_BAJIO, banco_BAJIO),
    (banco_BAMSA, banco_BAMSA),
    (banco_BANAMEX, banco_BANAMEX),
    (banco_BANCOMEXT, banco_BANCOMEXT),
    (banco_BANCOPPEL, banco_BANCOPPEL),
    (banco_BANJERCITO, banco_BANJERCITO),
    (banco_BANKAOOL, banco_BANKAOOL),
    (banco_BANOBRAS, banco_BANOBRAS),
    (banco_BANORTE, banco_BANORTE),
    (banco_BANREGIO, banco_BANREGIO),
    (banco_BANSEFI, banco_BANSEFI),
    (banco_BANSI, banco_BANSI),
    (banco_BARCLAYS, banco_BARCLAYS),
    (banco_BBASE, banco_BBASE),
    (banco_BBVABANCOMER, banco_BBVABANCOMER),
    (banco_BIM, banco_BIM),
    (banco_BMONEX, banco_BMONEX),
    (banco_BMULTIVA, banco_BMULTIVA),
    (banco_BULLTICKCB, banco_BULLTICKCB),
    (banco_INBURSA, banco_INBURSA),
    (banco_INTERCAM, banco_INTERCAM),
    (banco_VANGUARDIA, banco_VANGUARDIA),
    (banco_CBACTINBER, banco_CBACTINBER),
    (banco_CBBASE, banco_CBBASE),
    (banco_CBDEUTSCHE, banco_CBDEUTSCHE),
    (banco_CIBanco, banco_CIBanco),
    (banco_CLS, banco_CLS),
    (banco_COMPARTAMOS, banco_COMPARTAMOS),
    (banco_CONSULTORÍA, banco_CONSULTORÍA),
    (banco_CREDITSUISSE, banco_CREDITSUISSE),
    (banco_DEUTSCHE, banco_DEUTSCHE),
    (banco_EVERCORE, banco_EVERCORE),
    (banco_FACIL, banco_FACIL),
    (banco_FAMSA, banco_FAMSA),
    (banco_FINAMEX, banco_FINAMEX),
    (banco_FINCOMUN, banco_FINCOMUN),
    (banco_GBM, banco_GBM),
    (banco_GEMONEY, banco_GEMONEY),
    (banco_HDISEGUROS, banco_HDISEGUROS),
    (banco_HIPOTECARIAFEDERAL, banco_HIPOTECARIAFEDERAL),
    (banco_HIPOTECARIASUCASITA, banco_HIPOTECARIASUCASITA),
    (banco_HSBC, banco_HSBC),
    (banco_INBURSA, banco_INBURSA),
    (banco_INDEVAL, banco_INDEVAL),
    (banco_ING, banco_ING),
    (banco_INTERACCIONES, banco_INTERACCIONES),
    (banco_INTERCAM, banco_INTERCAM),
    (banco_INVEX, banco_INVEX),
    (banco_IXE, banco_IXE),
    (banco_JPMORGAN, banco_JPMORGAN),
    (banco_JPMORGANCB, banco_JPMORGANCB),
    (banco_KUSPIT, banco_KUSPIT),
    (banco_LIBERTAD, banco_LIBERTAD),
    (banco_MASARICB, banco_MASARICB),
    (banco_MERRILLLYNCH, banco_MERRILLLYNCH),
    (banco_MIFEL, banco_MIFEL),
    (banco_MONEXCB, banco_MONEXCB),
    (banco_MULTIVA, banco_MULTIVA),
    (banco_N_A, banco_N_A),
    (banco_NAFIN, banco_NAFIN),
    (banco_OPCIONESEMPRESARIALESDELNOROESTE, banco_OPCIONESEMPRESARIALESDELNOROESTE),
    (banco_ORDER, banco_ORDER),
    (banco_PagaTodo, banco_PagaTodo),
    (banco_PRUDENTIAL, banco_PRUDENTIAL),
    (banco_REFORMA, banco_REFORMA),
    (banco_REGIONAL, banco_REGIONAL),
    (banco_SABADELL, banco_SABADELL),
    (banco_SANTANDER, banco_SANTANDER),
    (banco_SCOTIABANK, banco_SCOTIABANK),
    (banco_SEGMTY, banco_SEGMTY),
    (banco_SKANDIA, banco_SKANDIA),
    (banco_SKANDIA, banco_SKANDIA),
    (banco_SOFIEXPRESS, banco_SOFIEXPRESS),
    (banco_STERLING, banco_STERLING),
    (banco_STP, banco_STP),
    (banco_TELECOMM, banco_TELECOMM),
    (banco_TIBER, banco_TIBER),
    (banco_TOKYO, banco_TOKYO),
    (banco_UBSBANK, banco_UBSBANK),
    (banco_UNAGRA, banco_UNAGRA),
    (banco_UNICA, banco_UNICA),
    (banco_VALMEX, banco_VALMEX),
    (banco_VALUE, banco_VALUE),
    (banco_VEPORMAS, banco_VEPORMAS),
    (banco_VECTOR, banco_VECTOR),
    (banco_VOLKSWAGEN, banco_VOLKSWAGEN),
    (banco_WALMART, banco_WALMART),
    (banco_ZURICH, banco_ZURICH),
    (banco_ZURICHVI, banco_ZURICHVI),
)


def newIdentificadorForOrdenDeCompra():
    today = datetime.now()
    res = "OC-" + today.strftime("%y%m") + "-"
    res += "{:03d}".format(OrdenDeCompra.objects.filter(
        identificador__startswith=res).count() + 1)
    return res


def newIdentificadorForOrdenDeEntrada():
    today = datetime.now()
    res = "OE-" + today.strftime("%y%m") + "-"
    res += "{:03d}".format(OrdenDeEntrada.objects.filter(
        identificador__startswith=res).count() + 1)
    return res

# Create your models here.


class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=100)
    nombre = models.CharField(max_length=254, blank=True)
    rfc = models.CharField(max_length=13)
    telefono = models.CharField(max_length=10, blank=True)
    extension = models.CharField(max_length=5, blank=True)
    telefono_2 = models.CharField(max_length=10, blank=True)
    telefono_3 = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    contacto = models.CharField(max_length=250, blank=True)
    direccion = models.ForeignKey(
        Direccion, on_delete=models.PROTECT,
        related_name="proveedor")
    clabe = models.CharField(max_length=18, blank=True)
    banco = models.CharField(
        max_length=100, default=banco_BANAMEX, choices=bancos)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre', 'razon_social']

    def __str__(self):
        if self.nombre:
            return self.nombre
        else:
            return self.razon_social

    def __unicode__(self):
        return self.__str__()


class Pieza(models.Model):
    idpieza = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    precio = models.DecimalField(
        max_digits=13, decimal_places=2, default=0.0)
    porcentaje_de_iva = models.DecimalField(
        max_digits=4, decimal_places=2, default=16.0)
    minimo_inventario = models.PositiveSmallIntegerField(default=0)
    maximo_inventario = models.PositiveSmallIntegerField(default=0)
    sku = models.CharField(max_length=250, blank=True)
    descripcion = models.TextField(blank=True)
    proveedores = models.ManyToManyField(
        Proveedor, through='Proveedor_Piezas',
        through_fields=('pieza', 'proveedor'),
        related_name='piezas')
    claveprodserv = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="piezas_claveprodserv",
        limit_choices_to={'catalogo__idsat': 'ClaveProdServ'})
    claveunidad = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="piezas_claveunidad",
        limit_choices_to={'catalogo__idsat': 'ClaveUnidad'})
    impuesto = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="piezas_impuesto",
        limit_choices_to={'catalogo__idsat': 'Impuesto'})
    tipofactor = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="piezas_tipofactor",
        limit_choices_to={'catalogo__idsat': 'TipoFactor'})
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre', 'marca', 'modelo']

    def __str__(self):
        name = self.nombre
        if self.marca:
            name += " " + self.marca
        if self.modelo:
            name += " " + self.modelo
        return name

    def __unicode__(self):
        return self.__str__()

    def cantidadEnInventario(self):
        return self.entradas() - self.salidas()

    def entradas(self):
        res = 0
        for oep in self.ordenes_de_entrada_en_que_llega.all():
            res += oep.cantidad
        return res

    def salidas(self):
        res = 0
        return res


class Proveedor_Piezas(models.Model):
    idproveedor_piezas = models.AutoField(primary_key=True)
    pieza = models.ForeignKey(
        Pieza,
        on_delete=models.CASCADE,
        related_name="pp_provedores")
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,
        related_name="pp_piezas")
    costo = models.DecimalField(
        max_digits=13, decimal_places=2, default=0.0)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['proveedor', 'pieza']

    def __str__(self):
        return "{} - {} (${})".format(
            self.proveedor, self.pieza, self.costo)

    def __unicode__(self):
        return self.__str__()


class OrdenDeCompra(models.Model):
    idordendecompra = models.AutoField(primary_key=True)
    identificador = models.CharField(max_length=50, blank=True)
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.PROTECT,
        related_name="ordenesdecompra")
    fecha = models.DateField(default=date.today)
    piezas = models.ManyToManyField(
        Pieza, through='Piezas_OrdenDeCompra',
        through_fields=('ordendecompra', 'pieza'),
        related_name='ordenes_de_compra')
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha', 'proveedor']

    def __str__(self):
        return "({}) {} - {}".format(
            self.identificador, self.proveedor, self.fecha)

    def __unicode__(self):
        return self.__str__()


class Piezas_OrdenDeCompra(models.Model):
    idpiezas_ordendecompra = models.AutoField(primary_key=True)
    pieza = models.ForeignKey(
        Pieza,
        on_delete=models.CASCADE,
        related_name="ordenesdecompra_en_que_se_requiere")
    ordendecompra = models.ForeignKey(
        OrdenDeCompra,
        on_delete=models.CASCADE,
        related_name="piezas_requeridas")
    cantidad = models.PositiveSmallIntegerField(default=0)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ordendecompra', 'pieza']

    def __str__(self):
        return "{} - {}".format(self.ordendecompra, self.pieza)

    def __unicode__(self):
        return self.__str__()


class OrdenDeEntrada(models.Model):
    idordendeentrada = models.AutoField(primary_key=True)
    identificador = models.CharField(max_length=50, blank=True)
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.PROTECT,
        related_name="ordenesdeentrada")
    fecha = models.DateField(default=date.today)
    piezas = models.ManyToManyField(
        Pieza, through='Piezas_OrdenDeEntrada',
        through_fields=('ordendeentrada', 'pieza'),
        related_name='ordenes_de_entrada')
    orden_de_compra = models.ForeignKey(
        OrdenDeCompra, on_delete=models.PROTECT, null=True, blank=True,
        related_name='orden_de_entrada',
        limit_choices_to={'orden_de_entrada__isnull': True})
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha', 'proveedor']

    def __str__(self):
        return "({}) {} - {}".format(
            self.identificador, self.proveedor, self.fecha)

    def __unicode__(self):
        return self.__str__()

    def piezas_total(self):
        res = Decimal(0.0)
        for pza in self.piezas_entradas.all():
            res += pza.cantidad
        return res

    def importe_total(self):
        res = Decimal(0.0)
        for pza in self.piezas_entradas.all():
            res += pza.importe
        return res


class Piezas_OrdenDeEntrada(models.Model):
    idpiezas_ordendeentrada = models.AutoField(primary_key=True)
    pieza = models.ForeignKey(
        Pieza,
        on_delete=models.CASCADE,
        related_name='ordenes_de_entrada_en_que_llega')
    ordendeentrada = models.ForeignKey(
        OrdenDeEntrada,
        on_delete=models.CASCADE,
        related_name="piezas_entradas")
    cantidad = models.PositiveSmallIntegerField(default=0)
    costo = models.DecimalField(
        max_digits=13, decimal_places=2, default=0.0)
    importe = models.DecimalField(
        max_digits=13, decimal_places=2, default=0.0)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ordendeentrada', 'pieza']

    def __str__(self):
        return "{} - {}".format(self.ordendecompra, self.pieza)

    def __unicode__(self):
        return self.__str__()
