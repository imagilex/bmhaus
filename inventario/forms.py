from django import forms

from .models import Proveedor, Pieza, OrdenDeCompra, OrdenDeEntrada


class FrmPieza(forms.ModelForm):

    class Meta:
        model = Pieza
        fields = [
            'nombre',
            'marca',
            'modelo',
            'precio',
            'porcentaje_de_iva',
            'claveprodserv',
            'claveunidad',
            'impuesto',
            'tipofactor',
        ]
        labels = {
            'porcentaje_de_iva': 'IVA',
            'claveprodserv': 'Clave del Producto',
            'claveunidad': 'Clave de la Unidad',
            'impuesto': 'Impuesto',
            'tipofactor': 'Tipo de Factor',
        }


class FrmProveedor(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = [
            'nombre',
            'razon_social',
            'rfc',
            'telefono',
            'extension',
        ]
        labels = {
            'rfc': 'RFC',
            'telefono': 'Teléfono',
            'extension': 'Extensión'
        }
        widgets = {
            'telefono': forms.TextInput(attrs={'type': 'tel'}),
            'extension': forms.TextInput(attrs={'type': 'number'}),
        }


class FrmOrdenDeCompra(forms.ModelForm):

    class Meta:
        model = OrdenDeCompra
        fields = [
            'proveedor',
            'fecha',
        ]
        widgets = {
            'fecha': forms.TextInput(attrs={'type': 'date'}),
        }


class FrmOrdenDeEntrada(forms.ModelForm):

    class Meta:
        model = OrdenDeEntrada
        fields = [
            'proveedor',
            'fecha',
            'orden_de_compra',
        ]
        widgets = {
            'fecha': forms.TextInput(attrs={'type': 'date'}),
        }
