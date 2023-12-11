from django import forms

from App.models import Cliente, Producto, Comentarios


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    dni = forms.CharField(max_length=10)
    email = forms.EmailField()


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ("usuario", "producto", "comentario")

class VentaForm(forms.Form):
    dni = forms.CharField(max_length=10)
    nombre_producto = forms.CharField(max_length=50)
    cantidad_vendida = forms.IntegerField()


class BuscarClienteForm(forms.Form):
    dni = forms.CharField()


