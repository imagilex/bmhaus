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
            'minimo_inventario',
            'maximo_inventario',
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
            'minimo_inventario': 'Número mínimo de piezas en inventario',
            'maximo_inventario': 'Número máximo de piezas en inventario',
        }
        help_texts = {
            'minimo_inventario': '0 para desactivar',
            'maximo_inventario': '0 para desactivar',
        }


class FrmProveedor(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = [
            'nombre',
            'razon_social',
            'rfc',
            'banco',
            'clabe',
            'contacto',
            'email',
            'telefono',
            'extension',
            'telefono_2',
            'telefono_3',
        ]
        labels = {
            'rfc': 'RFC',
            'telefono': 'Teléfono',
            'telefono_2': 'Teléfono 02',
            'telefono_3': 'Teléfono 03',
            'extension': 'Extensión',
            'clabe' : 'CLABE / Número de Cuenta'
        }
        widgets = {
            'telefono': forms.TextInput(attrs={'type': 'tel'}),
            'telefono_2': forms.TextInput(attrs={'type': 'tel'}),
            'telefono_3': forms.TextInput(attrs={'type': 'tel'}),
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


class FrmOrdenDeCompraSee(forms.ModelForm):

    class Meta:
        model = OrdenDeCompra
        fields = [
            'identificador',
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
            'orden_de_compra',
            'fecha',
        ]
        widgets = {
            'fecha': forms.TextInput(attrs={'type': 'date'}),
        }


class FrmOrdenDeEntradaSee(forms.ModelForm):

    class Meta:
        model = OrdenDeEntrada
        fields = [
            'identificador',
            'orden_de_compra',
            'proveedor',
            'fecha',
        ]
        widgets = {
            'fecha': forms.TextInput(attrs={'type': 'date'}),
        }
