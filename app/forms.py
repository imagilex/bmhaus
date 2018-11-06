from django import forms

from datetime import datetime

from .models import Cliente, Vehiculo, DoctoOrdenReparacion, AvanceEnFlujo

def theTime():
    t =  datetime.now()
    return "{:02d}:{:02d}".format(t.hour, t.minute)


class FrmCliente(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'usuario',
            'contraseña',
            'is_active',
            'first_name',
            'last_name',
            'apellido_materno',
            'email',
            'telefono',
            'celular',
            'telefono_oficina',
            'extension',
            'fotografia',
            'razon_social',
            'rfc',
            'formapago',
            'moneda',
            'metodopago',
            'residenciafiscal',
            'usocfdi',
            'claveprodserv',
            'claveunidad',
            'impuesto',
            'tipofactor'
        ]
        labels = {
            'email': 'E-Mail',
            'last_name': 'Apellido paterno',
            'rfc': 'RFC',
            'formapago': 'Forma de Pago',
            'moneda': 'Moneda',
            'metodopago': 'Método de Pago',
            'residenciafiscal': 'Residencia Fiscal',
            'usocfdi': 'Uso del CFDi',
            'claveprodserv': 'Clave del Producto o Servicio',
            'claveunidad': 'Clave de la Unidad',
            'impuesto': 'Impuesto',
            'tipofactor': 'Tipo de Factor',
        }
        help_texts = {
            'is_active': '',
        }
        widgets = {
            'telefono': forms.TextInput(attrs={'type': 'tel'}),
            'celular': forms.TextInput(attrs={'type': 'tel'}),
            'telefono_oficina': forms.TextInput(attrs={'type': 'tel'}),
            'extension': forms.TextInput(attrs={'type': 'number'}),
        }


class FrmClienteUsr(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'usuario',
            'contraseña',
            'is_active',
            'first_name',
            'last_name',
            'apellido_materno',
            'fotografia',
        ]
        labels = {
            'last_name': 'Apellido paterno',
        }
        help_texts = {
            'is_active': '',
        }


class FrmClienteContacto(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'email',
            'telefono',
            'celular',
            'telefono_oficina',
            'extension',
        ]
        labels = {
            'email': 'E-Mail',
        }
        widgets = {
            'telefono': forms.TextInput(attrs={'type': 'tel'}),
            'celular': forms.TextInput(attrs={'type': 'tel'}),
            'telefono_oficina': forms.TextInput(attrs={'type': 'tel'}),
            'extension': forms.TextInput(attrs={'type': 'number'}),
        }


class FrmClienteFacturacion(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'razon_social',
            'rfc',
            'formapago',
            'moneda',
            'metodopago',
            'residenciafiscal',
            'usocfdi',
            'claveprodserv',
            'claveunidad',
            'impuesto',
            'tipofactor'
        ]
        labels = {
            'rfc': 'RFC',
            'formapago': 'Forma de Pago',
            'moneda': 'Moneda',
            'metodopago': 'Método de Pago',
            'residenciafiscal': 'Residencia Fiscal',
            'usocfdi': 'Uso del CFDi',
            'claveprodserv': 'Clave del Producto o Servicio',
            'claveunidad': 'Clave de la Unidad',
            'impuesto': 'Impuesto',
            'tipofactor': 'Tipo de Factor',
        }


class FrmVehiculo(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = [
            'marca',
            'serie',
            'modelo',
            'año',
            'clase',
            'tipo',
            'color',
            'vin',
            'numero_de_placa',
            'fotografia'
        ]
        label = {
            'modelo': 'Versión'
        }


class FrmDoctoOrdenReparacion(forms.ModelForm):

    class Meta:
        model = DoctoOrdenReparacion
        fields = [
            'fecha_de_recepcion',
            'hora_de_recepcion',
            'servicio_solicitado',
            'fotografia_kilometros',
            'fotografia_tanque_de_gasolina',
            'fotografia_superior',
            'fotografia_frente',
            'fotografia_trasera',
            'fotografia_lateral_izquierdo',
            'fotografia_lateral_derecho',

            'unidad_de_luces',
            'cuartos',
            'antena',
            'espejo_lateral',
            'cristales',
            'emblema',
            'llantas',
            'tapon_de_ruedas',
            'molduras_completas',
            'tapon_de_gasolina',
            'carroceria_sin_golpes',
            'bocinas_de_claxon',
            'limpiadores',

            'instrumentos_de_tablero',
            'calefaccion',
            'radio',
            'bocinas',
            'encendedor',
            'espejo_retrovisor',
            'ceniceros',
            'cinturones',
            'botones_de_interiores',
            'manijas_de_interiores',
            'tapetes',
            'vestiduras',

            'gato',
            'maneral_de_gato',
            'llave_de_ruedas',
            'estuche_de_herramientas',
            'triangulo_de_seguridad',
            'llanta_de_refaccion',
            'extingidor',

            'claxon',
            'tapon_de_aceite',
            'tapon_de_radiador',
            'varilla_de_aceite',
            'filtro_de_aire',
            'bateria',

            'costo_de_revision',

            'firma_del_prestador_del_servicio',
            'firma_del_consumidor',
        ]
        widgets = {
            'fecha_de_recepcion': forms.TextInput(attrs={'type': 'date'}),
            'hora_de_recepcion': forms.TextInput(attrs={'type': 'time'}),
        }
        help_texts = {
            'costo_de_revision': "En caso de que el presupuesto no sea"
                "aceptado, el consumidor pagará exclusivamente el costo por"
                "la revisión y diagnóstico y el prestador del servicio se"
                "obliga a devolver el vehículo en las condiciones en las que"
                "le fue entregado, exceptuando las consecuencias inevitables"
                "del diagnóstico.",
        }


class FrmDoctoOrdenReparacionGenerales01(forms.ModelForm):

    class Meta:
        model = DoctoOrdenReparacion
        fields = [
            'fecha_de_recepcion',
            'hora_de_recepcion',
            'servicio_solicitado',
            'costo_de_revision',
        ]
        widgets = {
            'fecha_de_recepcion': forms.TextInput(attrs={'type': 'date'}),
            'hora_de_recepcion': forms.TextInput(attrs={'type': 'time', 'value':theTime}),
        }
        help_texts = {
            'costo_de_revision': "En caso de que el presupuesto no sea"
                "aceptado, el consumidor pagará exclusivamente el costo por"
                "la revisión y diagnóstico y el prestador del servicio se"
                "obliga a devolver el vehículo en las condiciones en las que"
                "le fue entregado, exceptuando las consecuencias inevitables"
                "del diagnóstico.",
        }


class FrmDoctoOrdenReparacionGenerales02(forms.ModelForm):

    class Meta:
        model = DoctoOrdenReparacion
        fields = [
            'fotografia_kilometros',
            'fotografia_tanque_de_gasolina',
            'fotografia_superior',
            'fotografia_frente',
            'fotografia_trasera',
            'fotografia_lateral_izquierdo',
            'fotografia_lateral_derecho',
        ]


class FrmDoctoOrdenReparacionExteriores(forms.ModelForm):

    class Meta:
        model = DoctoOrdenReparacion
        fields = [
            'unidad_de_luces',
            'cuartos',
            'antena',
            'espejo_lateral',
            'cristales',
            'emblema',
            'llantas',
            'tapon_de_ruedas',
            'molduras_completas',
            'tapon_de_gasolina',
            'carroceria_sin_golpes',
            'bocinas_de_claxon',
            'limpiadores',
        ]


class FrmDoctoOrdenReparacionInteriores(forms.ModelForm):

    class Meta:
        model = DoctoOrdenReparacion
        fields = [
            'instrumentos_de_tablero',
            'calefaccion',
            'radio',
            'bocinas',
            'encendedor',
            'espejo_retrovisor',
            'ceniceros',
            'cinturones',
            'botones_de_interiores',
            'manijas_de_interiores',
            'tapetes',
            'vestiduras',
        ]


class FrmDoctoOrdenReparacionAccesorios(forms.ModelForm):

    class Meta:
        model = DoctoOrdenReparacion
        fields = [
            'gato',
            'maneral_de_gato',
            'llave_de_ruedas',
            'estuche_de_herramientas',
            'triangulo_de_seguridad',
            'llanta_de_refaccion',
            'extingidor',
        ]


class FrmDoctoOrdenReparacionComponentesMecanicos(forms.ModelForm):

    class Meta:
        model = DoctoOrdenReparacion
        fields = [
            'claxon',
            'tapon_de_aceite',
            'tapon_de_radiador',
            'varilla_de_aceite',
            'filtro_de_aire',
            'bateria',
        ]


class FrmDoctoOrdenReparacionFirmas(forms.ModelForm):

    class Meta:
        model = DoctoOrdenReparacion
        fields = [
            'firma_del_prestador_del_servicio',
            'firma_del_consumidor',
        ]


class FrmAvanceEnFlujo(forms.ModelForm):

    class Meta:
        model = AvanceEnFlujo
        fields = [
            'nota',
            'fotografia',
        ]
