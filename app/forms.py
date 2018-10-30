from django import forms

from .models import Cliente, Vehiculo


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
