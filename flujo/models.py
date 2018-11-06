from django.db import models

from initsys.models import Usr

# Create your models here.


class Flujo(models.Model):
    idflujo = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, default="")
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return "{}".format(self.nombre)

    def __unicode__(self):
        return self.__str__()


class Estado(models.Model):
    idestado = models.AutoField(primary_key=True)
    flujo = models.ForeignKey(
        Flujo, on_delete=models.PROTECT,
        related_name="estados")
    name = models.CharField(max_length=250, default="")
    nombre = models.CharField(max_length=250)
    no_estado = models.PositiveSmallIntegerField(default=0)
    es_inicial = models.BooleanField(default=False)
    es_final = models.BooleanField(default=False)
    es_cancelacion = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['flujo', 'no_estado', 'idestado']

    def __str__(self):
        return "{}".format(self.nombre)

    def __unicode__(self):
        return self.__str__()


class Accion(models.Model):
    idaccion = models.AutoField(primary_key=True)
    flujo = models.ForeignKey(
        Flujo, on_delete=models.PROTECT,
        related_name="acciones")
    name = models.CharField(max_length=250, default="")
    nombre = models.CharField(max_length=250)
    estado_inicial = models.ForeignKey(
        Estado, on_delete=models.PROTECT,
        related_name="acciones_ejecutar")
    estado_final = models.ForeignKey(
        Estado, on_delete=models.PROTECT,
        related_name="acciones_ejecutadas")
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['flujo', 'nombre', 'idaccion']

    def __str__(self):
        return "{}".format(self.nombre)

    def __unicode__(self):
        return self.__str__()


class InstanciaFlujo(models.Model):
    idinstanciaflujo = models.AutoField(primary_key=True)
    flujo = models.ForeignKey(
        Flujo, on_delete=models.PROTECT,
        related_name="instancias")
    tipo_instancia = models.CharField(max_length=250)
    estado_actual = models.ForeignKey(
        Estado, on_delete=models.PROTECT,
        related_name="instancias_en_estado")
    terminado = models.BooleanField(default=False)
    extra_data = models.TextField(blank=True)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['flujo', 'tipo_instancia', 'idinstanciaflujo']

    def __str__(self):
        return "{} ({})".format(self.tipo_instancia, self.idinstanciaflujo)

    def __unicode__(self):
        return self.__str__()


class InstanciaHistoria(models.Model):
    idinstanciahistoria = models.AutoField(primary_key=True)
    instanciaflujo = models.ForeignKey(
        InstanciaFlujo,
        on_delete=models.CASCADE, related_name="historia")
    accion = models.ForeignKey(
        Accion, on_delete=models.PROTECT,
        related_name="instancias_aplicadoras")
    extra_data = models.TextField(blank=True)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['instanciaflujo', 'created_at', 'accion', 'idinstanciahistoria']

    def __str__(self):
        return "{}".format(self.accion)

    def __unicode__(self):
        return self.__str__()


class InstanciaHistoriaDetalle(models.Model):
    idinstanciahistoriadetalle = models.AutoField(primary_key=True)
    instanciahistoria = models.ForeignKey(
        InstanciaHistoria,
        on_delete=models.CASCADE, related_name="historia_detalle")
    iddocumento_generado = models.CharField(max_length=250)
    tipo_documento_generado = models.CharField(max_length=250)
    extra_data = models.TextField(blank=True)
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
            'instanciahistoria',
            'tipo_documento_generado',
            'iddocumento_generado',
            'idinstanciahistoriadetalle']

    def __str__(self):
        return "{} ({})".format(
            self.tipo_documento_generado, self.iddocumento_generado)

    def __unicode__(self):
        return self.__str__()
