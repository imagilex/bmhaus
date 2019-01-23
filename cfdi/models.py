from django.db import models

from datetime import datetime

from initsys.models import Usr

# Create your models here.


def catCFDI(catalogo):
    catalogo = CatalogoSAT.objects.filter(idsat=catalogo)
    if catalogo.exists():
        catalogo = catalogo[0]
        return [
            (opc.clave_sat, opc.mostrar_como)
            for opc in OpcionCatalogoSAT.objects.filter(catalogo=catalogo)]
    return []


def catCFDI_ClaveProdServ():
    return catCFDI('ClaveProdServ')


def catCFDI_ClaveUnidad():
    return catCFDI('ClaveUnidad')


def catCFDI_FormaPago():
    return catCFDI('FormaPago')


def catCFDI_Impuesto():
    return catCFDI('Impuesto')


def catCFDI_MetodoPago():
    return catCFDI('MetodoPago')


def catCFDI_Moneda():
    return catCFDI('Moneda')


def catCFDI_Pais():
    return catCFDI('Pais')


def catCFDI_RegimenFiscal():
    return catCFDI('RegimenFiscal')


def catCFDI_TipoDeComprobante():
    return catCFDI('TipoDeComprobante')


def catCFDI_TipoFactor():
    return catCFDI('TipoFactor')


def catCFDI_TipoRelacion():
    return catCFDI('TipoRelacion')


def catCFDI_UsoCFDI():
    return catCFDI('UsoCFDI')


class CatalogoSAT(models.Model):
    idcatalogo = models.AutoField(primary_key=True)
    idsat = models.CharField(max_length=250)
    nombre = models.CharField(max_length=250)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()


class OpcionCatalogoSAT(models.Model):
    idopcion = models.AutoField(primary_key=True)
    catalogo = models.ForeignKey(
        CatalogoSAT, on_delete=models.CASCADE,
        related_name="opciones")
    clave_sat = models.CharField(max_length=25)
    descipcion = models.CharField(max_length=250)
    mostrar_como = models.CharField(max_length=250)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['catalogo', 'mostrar_como']

    def __str__(self):
        return "{}".format(self.mostrar_como)

    def __unicode__(self):
        return self.__str__()


class Comprobante(models.Model):
    """
    Estándar de Comprobante Fiscal Digital por Internet

    Secuencia(1,1)
        CfdiRelacionados(0,1)
        Emisor(1,1)
        Receptor(1,1)
        Conceptos(1,1)
        Impuestos(0,1)
        Complemento(0,1)
        Addenda(0,1)
    """
    idcomprobante = models.AutoField(primary_key=True)
    Version = models.CharField(max_length=5, default="3.3")
    Serie = models.CharField(max_length=25, null=True, blank=True)
    Folio = models.CharField(max_length=40, null=True, blank=True)
    Fecha = models.DateTimeField(default=datetime.now)
    Sello = models.TextField(null=True, blank=True)
    FormaPago = models.CharField(max_length=25, null=True, blank=True)
    FormaPago_txt = models.CharField(max_length=250, null=True, blank=True)
    FormaPago_opcion = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        related_name="comprobantes_formapago", null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'FormaPago'})
    NoCertificado = models.CharField(max_length=20, null=True, blank=True)
    Certificado = models.TextField(null=True, blank=True)
    CondicionesDePago = models.CharField(
        max_length=1000, null=True, blank=True)
    SubTotal = models.DecimalField(max_digits=13, decimal_places=2)
    Descuento = models.DecimalField(
        null=True, blank=True, max_digits=13, decimal_places=2)
    Moneda = models.CharField(max_length=25, null=True, blank=True)
    Moneda_txt = models.CharField(max_length=250, null=True, blank=True)
    Moneda_opcion = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        related_name="comprobantes_moneda", null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'Moneda'})
    TipoCambio = models.DecimalField(
        null=True, blank=True, max_digits=11, decimal_places=6)
    Total = models.DecimalField(max_digits=13, decimal_places=2)
    TipoDeComprobante = models.CharField(max_length=25)
    TipoDeComprobante_txt = models.CharField(max_length=250)
    TipoDeComprobante_opcion = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        related_name="comprobantes_tipodecomprobante",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'TipoDeComprobante'})
    MetodoPago = models.CharField(max_length=25, null=True, blank=True)
    MetodoPago_txt = models.CharField(
        max_length=250, null=True, blank=True)
    MetodoPago_opcion = models.ForeignKey(
        OpcionCatalogoSAT, on_delete=models.SET_NULL,
        related_name="comprobantes_metodopago",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'MetodoPago'})
    LugarExpedicion = models.CharField(max_length=5)
    Confirmacion = models.CharField(max_length=5, null=True, blank=True)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            'Serie', 'Folio', '-Fecha', '-created_at', '-updated_at']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class CfdiRelacionados(models.Model):
    """
    Nodo opcional para precisar la información de los comprobantes
    relacionados

    Secuencia(1,1)
        CfdiRelacionado(1,Ilimitado)
    """
    idcfdirelacionados = models.AutoField(primary_key=True)
    comprobante = models.ForeignKey(
        Comprobante, on_delete=models.CASCADE,
        related_name="nodo_cfdisrelacionados")
    TipoRelacion = models.CharField(max_length=25)
    TipoRelacion_txt = models.CharField(max_length=250)
    TipoRelacion_opcion = models.ForeignKey(
        OpcionCatalogoSAT,
        on_delete=models.SET_NULL,
        related_name="cfdisrelacionados_tiporelacion",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'TipoRelacion'})
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['TipoRelacion']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        pass

    def isValidCFDi(self):
        pass

    def cadenaOriginal(self):
        pass


class CfdiRelacionado(models.Model):
    """
    Nodo requerido para precisar la información de los comprobantes
    relacionados
    """
    idcfdirelacionado = models.AutoField(primary_key=True)
    cfdirelacionados = models.ForeignKey(
        CfdiRelacionados,
        on_delete=models.CASCADE, related_name="cfdisrelacionados")
    UUID = models.CharField(max_length=36)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['UUID']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class Emisor(models.Model):
    """
    Nodo requerido para expresar la información del contribuyente emisor
    del comprobante
    """
    idemisor = models.AutoField(primary_key=True)
    comprobante = models.ForeignKey(
        Comprobante, on_delete=models.CASCADE,
        related_name="emisor")
    Rfc = models.CharField(max_length=13)
    Nombre = models.CharField(max_length=254, null=True, blank=True)
    RegimenFiscal = models.CharField(max_length=25)
    RegimenFiscal_txt = models.CharField(max_length=250)
    RegimenFiscal_opcion = models.ForeignKey(
        OpcionCatalogoSAT,
        on_delete=models.SET_NULL, related_name="emisor_regimenfiscal",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'RegimenFiscal'})
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['Nombre', 'Rfc']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class Receptor(models.Model):
    """
    Nodo requerido para precisar la información del contribuyente receptor
    del comprobante
    """
    idreceptor = models.AutoField(primary_key=True)
    comprobante = models.ForeignKey(
        Comprobante, on_delete=models.CASCADE,
        related_name="receptor")
    Rfc = models.CharField(max_length=13)
    Nombre = models.CharField(max_length=254, null=True, blank=True)
    ResidenciaFiscal = models.CharField(
        max_length=25,
        null=True, blank=True)
    ResidenciaFiscal_txt = models.CharField(
        max_length=250,
        null=True, blank=True)
    ResidenciaFiscal_opcion = models.ForeignKey(
        OpcionCatalogoSAT,
        on_delete=models.SET_NULL,
        related_name="receptor_residenciafiscal",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'ResidenciaFiscal'})
    NumRegIdTrib = models.CharField(max_length=40, null=True, blank=True)
    UsoCFDI = models.CharField(max_length=25)
    UsoCFDI_txt = models.CharField(max_length=250)
    UsoCFDI_opcion = models.ForeignKey(
        OpcionCatalogoSAT,
        on_delete=models.SET_NULL, related_name="receptor_usocfdi",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'UsoCFDI'})
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['Nombre', 'Rfc']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class Conceptos(models.Model):
    """
    Nodo requerido para listar los conceptos cubiertos por el comprobante

    Secuencia(1,1)
        Concepto(1,Ilimitado)
    """
    idconceptos = models.AutoField(primary_key=True)
    comprobante = models.ForeignKey(
        Comprobante, on_delete=models.CASCADE,
        related_name="nodo_conceptos")
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['idconceptos']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class Concepto(models.Model):
    """
    Nodo requerido para registrar la información detallada de un bien o
    servicio amparado en el comprobante

    Secuencia(1,1)
        CImpuestos(0,1)
        InformacionAduanera(0,Ilimitado)
        CuentaPredial(0,1)
        ComplementoConcepto(0,1)
        Parte(0,Ilimitado)
    """
    idconcepto = models.AutoField(primary_key=True)
    conceptos = models.ForeignKey(
        Conceptos, on_delete=models.CASCADE,
        related_name="conceptos")
    ClaveProdServ = models.CharField(max_length=25)
    ClaveProdServ_txt = models.CharField(max_length=250)
    ClaveProdServ_opcion = models.ForeignKey(
        OpcionCatalogoSAT,
        on_delete=models.SET_NULL, related_name="concepto_claveprodserv",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'ClaveProdServ'})
    NoIdentificacion = models.CharField(
        max_length=100, null=True, blank=True)
    Cantidad = models.DecimalField(max_digits=12, decimal_places=2)
    ClaveUnidad = models.CharField(max_length=25)
    ClaveUnidad_txt = models.CharField(max_length=250)
    ClaveUnidad_opcion = models.ForeignKey(
        OpcionCatalogoSAT,
        on_delete=models.SET_NULL, related_name="concepto_claveunidad",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'ClaveUnidad'})
    Unidad = models.CharField(max_length=20, null=True, blank=True)
    Descripcion = models.CharField(max_length=1000)
    ValorUnitario = models.DecimalField(max_digits=13, decimal_places=2)
    Importe = models.DecimalField(max_digits=13, decimal_places=2)
    Descuento = models.DecimalField(
        max_digits=13, decimal_places=2,
        null=True, blank=True)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ClaveProdServ_txt', 'NoIdentificacion', 'Descripcion']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class CImpuestos(models.Model):
    """
    Nodo opcional para capturar los impuestos aplicables al presente
    concepto. Cuando un concepto no registra un impuesto, implica que no es
    objeto del mismo

    Secuencia(1,1)
        CTraslados(0,1)
        CRetenciones(0,1)
    """
    idcimpuestos = models.AutoField(primary_key=True)
    concepto = models.ForeignKey(
        Concepto, on_delete=models.CASCADE,
        related_name="nodo_cimpuestos", null=True, blank=True)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['idcimpuestos']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class CTraslados(models.Model):
    """
    Nodo opcional para asentar los impuestos trasladados aplicables al
    presente concepto

    Secuencia(1,1)
        CTraslado(1,Ilimitado)
    """
    idctraslados = models.AutoField(primary_key=True)
    cimpuestos = models.ForeignKey(
        CImpuestos, on_delete=models.CASCADE,
        related_name="nodo_ctraslados")
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['idctraslados']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class CTraslado(models.Model):
    """
    Nodo requerido para asentar la información detallada de un trasladado
    de impuestos aplicable al presente concepto
    """
    idctraslado = models.AutoField(primary_key=True)
    ctraslados = models.ForeignKey(
        CTraslados, on_delete=models.CASCADE,
        related_name="ctraslados")
    Base = models.DecimalField(max_digits=13, decimal_places=2)
    Impuesto = models.CharField(max_length=25)
    Impuesto_txt = models.CharField(max_length=250)
    Impuesto_opcion = models.ForeignKey(
        OpcionCatalogoSAT,
        on_delete=models.SET_NULL, related_name="ctraslado_impuesto",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'Impuesto'})
    TipoFactor = models.CharField(max_length=25)
    TipoFactor_txt = models.CharField(max_length=250)
    TipoFactor_opcion = models.ForeignKey(
        OpcionCatalogoSAT,
        on_delete=models.SET_NULL, related_name="ctraslado_tipofactor",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'TipoFactor'})
    TasaOCuota = models.DecimalField(
        max_digits=9, decimal_places=2,
        null=True, blank=True)
    Importe = models.DecimalField(
        max_digits=13, decimal_places=2,
        null=True, blank=True)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['Impuesto_txt', 'TipoFactor_txt']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class CRetenciones(models.Model):
    """
    Nodo opcional para asentar los impuestos retenidos aplicables al
    presente concepto

    Secuencia(1,1)
        CRetencion(1,Ilimitado)
    """
    idcretenciones = models.AutoField(primary_key=True)
    cimpuestos = models.ForeignKey(
        CImpuestos, on_delete=models.CASCADE,
        related_name="nodo_cretenciones")
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['idcretenciones']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class CRetencion(models.Model):
    """
    Nodo requerido para asentar la información detallada de una retención
    de impuestos aplicable al presente concepto
    """
    idcretencion = models.AutoField(primary_key=True)
    cretenciones = models.ForeignKey(
        CRetenciones,
        on_delete=models.CASCADE, related_name="cretenciones")
    Base = models.DecimalField(max_digits=13, decimal_places=2)
    Impuesto = models.CharField(max_length=25)
    Impuesto_txt = models.CharField(max_length=250)
    Impuesto_opcion = models.ForeignKey(
        OpcionCatalogoSAT,
        on_delete=models.SET_NULL, related_name="cretencion_impuesto",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'Impuesto'})
    TipoFactor = models.CharField(max_length=25)
    TipoFactor_txt = models.CharField(max_length=250)
    TipoFactor_opcion = models.ForeignKey(
        OpcionCatalogoSAT,
        on_delete=models.SET_NULL, related_name="cretencion_tipofactor",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'TipoFactor'})
    TasaOCuota = models.DecimalField(max_digits=9, decimal_places=2)
    Importe = models.DecimalField(max_digits=13, decimal_places=2)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['Impuesto_txt', 'TipoFactor_txt']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class CuentaPredial(models.Model):
    """
    Nodo opcional para asentar el número de cuenta predial con el que fue
    registrado el inmueble, en el sistema catastral de la entidad
    federativa de que trate, o bien para incorporar los datos de
    identificación del certificado de participación inmobiliaria no
    amortizable
    """
    idcuentapredial = models.AutoField(primary_key=True)
    concepto = models.ForeignKey(
        Concepto, on_delete=models.CASCADE,
        related_name="cuentasprediales")
    Numero = models.CharField(max_length=150)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['Numero']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class ComplementoConcepto(models.Model):
    """
    Nodo opcional donde se incluyen los nodos complementarios de extensión
    al concepto definidos por el SAT, de acuerdo con las disposiciones
    particulares para un sector o actividad específica
    """
    idcomplementoconcepto = models.AutoField(primary_key=True)
    concepto = models.ForeignKey(
        Concepto, on_delete=models.CASCADE,
        related_name="complementos")
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['idcomplementoconcepto']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class Parte(models.Model):
    """
    Nodo opcional para expresar las partes o componentes que integran la
    totalidad del concepto expresado en el comprobante fiscal digital por
    internet
    """
    idparte = models.AutoField(primary_key=True)
    concepto = models.ForeignKey(
        Concepto, on_delete=models.CASCADE,
        related_name="partes")
    ClaveProdServ = models.CharField(max_length=25)
    ClaveProdServ_txt = models.CharField(max_length=250)
    ClaveProdServ_opcion = models.ForeignKey(
        OpcionCatalogoSAT,
        on_delete=models.SET_NULL, related_name="parte_claveprodserv",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'ClaveProdServ'})
    NoIdentificacion = models.CharField(
        max_length=100,
        null=True, blank=True)
    Cantidad = models.DecimalField(max_digits=12, decimal_places=2)
    Unidad = models.CharField(max_length=20, null=True, blank=True)
    Descripcion = models.CharField(max_length=1000)
    ValorUnitario = models.DecimalField(
        max_digits=13, decimal_places=2,
        null=True, blank=True)
    Importe = models.DecimalField(
        max_digits=13, decimal_places=2,
        null=True, blank=True)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ClaveProdServ_txt', 'NoIdentificacion', 'Descripcion']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class InformacionAduanera(models.Model):
    """
    Concepto
    Parte
        Nodo opcional para introducir la información aduanera aplicable
        cuando se trate de ventas de primera mano de mercancias importadas
        o se trate de operaciones de comercio exterior con bienes o
        servicios
    """
    idinformacionaduanera = models.AutoField(primary_key=True)
    concepto = models.ForeignKey(
        Concepto, on_delete=models.CASCADE,
        related_name="cinformacionesaduaneras", null=True, blank=True)
    parte = models.ForeignKey(
        Parte, on_delete=models.CASCADE,
        related_name="pinformacionesaduaneras", null=True, blank=True)
    NumeroPedimento = models.CharField(max_length=21)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['NumeroPedimento']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class Impuestos(models.Model):
    """
    Nodo condicional para expresar el resumen de los impuestos aplicables

    Secuencia(1,1)
        Retenciones(0,1)
        Traslados(0,1)
    """
    idimpuestos = models.AutoField(primary_key=True)
    comprobante = models.ForeignKey(
        Comprobante, on_delete=models.CASCADE,
        related_name="nodo_impuestos", null=True, blank=True)
    TotalImpuestosRetenidos = models.DecimalField(
        max_digits=13,
        decimal_places=2, null=True, blank=True)
    TotalImpuestosTrasladados = models.DecimalField(
        max_digits=13,
        decimal_places=2, null=True, blank=True)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['idimpuestos']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class Traslados(models.Model):
    """
    Nodo condicional para capturar los impuestos trasladados aplicables. Es
    requerido cuando en los conceptos se registre un impuesto trasladado

    Secuencia(1,1)
        Traslado(1,Ilimitado)
    """
    idtraslados = models.AutoField(primary_key=True)
    impuestos = models.ForeignKey(
        Impuestos, on_delete=models.CASCADE,
        related_name="nodo_traslados")
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['idtraslados']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class Traslado(models.Model):
    """
    Nodo requerido para la información detallada de un trasladado de
    impuesto específico
    """
    idtraslado = models.AutoField(primary_key=True)
    traslados = models.ForeignKey(
        Traslados, on_delete=models.CASCADE,
        related_name="trasladados")
    Impuesto = models.CharField(max_length=25)
    Impuesto_txt = models.CharField(max_length=250)
    Impuesto_opcion = models.ForeignKey(
        OpcionCatalogoSAT,
        on_delete=models.SET_NULL, related_name="traslado_impuesto",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'Impuesto'})
    TipoFactor = models.CharField(max_length=25)
    TipoFactor_txt = models.CharField(max_length=250)
    TipoFactor_opcion = models.ForeignKey(
        OpcionCatalogoSAT,
        on_delete=models.SET_NULL, related_name="traslado_tipofactor",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'TipoFactor'})
    TasaOCuota = models.DecimalField(max_digits=9, decimal_places=2)
    Importe = models.DecimalField(max_digits=13, decimal_places=2)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['Impuesto_txt', 'TipoFactor_txt']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class Retenciones(models.Model):
    """
    Nodo condicional para capturar los impuestos retenidos aplicables. Es
    requerido cuando en los conceptos se registre algún impuesto retenido

    Secuencia(1,1)
        Retencion(1,Ilimitado)
    """
    idretenciones = models.AutoField(primary_key=True)
    impuestos = models.ForeignKey(
        Impuestos, on_delete=models.CASCADE,
        related_name="nodo_retenciones")
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['idretenciones']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class Retencion(models.Model):
    """
    Nodo requerido para la información detallada de una retención de
    impuesto específico
    """
    idretencion = models.AutoField(primary_key=True)
    retenciones = models.ForeignKey(
        Retenciones, on_delete=models.CASCADE,
        related_name="retenciones")
    Impuesto = models.CharField(max_length=25)
    Impuesto_txt = models.CharField(max_length=250)
    Impuesto_opcion = models.ForeignKey(
        OpcionCatalogoSAT,
        on_delete=models.SET_NULL, related_name="retencion_impuesto",
        null=True, blank=True,
        limit_choices_to={'catalogo__idsat': 'Impuesto'})
    Importe = models.DecimalField(max_digits=13, decimal_places=2)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['Impuesto_txt']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class Complemento(models.Model):
    """
    Nodo opcional donde se incluye el complemento Timbre Fiscal Digital de
    manera obligatoria y los nodos complementarios determinados por el SAT,
    de acuerdo con las disposiciones particulares para un sector o
    actividad específica
    """
    idcomplemento = models.AutoField(primary_key=True)
    comprobante = models.ForeignKey(
        Comprobante, on_delete=models.CASCADE,
        related_name="complementos")
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['idcomplemento']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""


class Addenda(models.Model):
    """
    Nodo opcional para recibir las extensiones al presente formato que sean
    de utilidad al contribuyente. Para las reglas de uso del mismo,
    referirse al formato origen
    """
    idaddenda = models.AutoField(primary_key=True)
    comprobante = models.ForeignKey(
        Comprobante, on_delete=models.CASCADE,
        related_name="addendas")
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['idaddenda']

    def __str__(self):
        return ""

    def __unicode__(self):
        return self.__str__()

    def isValid(self):
        return True

    def isValidCFDi(self):
        return True

    def cadenaOriginal(self):
        return ""
