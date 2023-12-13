from django import forms

from App.models import Cliente, Producto, Comentarios


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    dni = forms.CharField(max_length=10)
    email = forms.EmailField()


class ProductoForm(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 400px;'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 6}))
    class Meta:
        model = Producto
        fields = '__all__'


class ComentarioForm(forms.ModelForm):
    comentario = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 8}))
    usuario = forms.ModelChoiceField(queryset=None, widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Comentarios
        fields = ["usuario", "comentario"]


class VentaForm(forms.Form):
    dni = forms.CharField(max_length=10)
    nombre_producto = forms.CharField(max_length=50)
    cantidad_vendida = forms.IntegerField()


class BuscarClienteForm(forms.Form):
    dni = forms.CharField()


class BuscarProductoForm(forms.Form):
    titulo = forms.CharField()


