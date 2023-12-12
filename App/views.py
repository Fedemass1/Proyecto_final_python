from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from App.models import Cliente, Producto, Venta, Comentarios
from App.forms import (ClienteForm, VentaForm,
                       BuscarClienteForm, ComentarioForm, ProductoForm, BuscarProductoForm)


def show_html(request):
    contexto = {

    }
    return render(request, 'index.html', contexto)

@login_required
def mostrar_clientes(request):
    clientes = Cliente.objects.all()
    contexto = {
        "clientes": clientes,
        "form": BuscarClienteForm,
    }

    return render(request, "App/mostrar_clientes.html", contexto)

@login_required
def agregar_cliente_form(request):
    cliente = ClienteForm
    contexto = {
        "form": cliente
    }

    if request.method == "POST":
        cliente = ClienteForm(request.POST)

        if cliente.is_valid():
            informacion = cliente.cleaned_data

            cliente_crear = Cliente(nombre=informacion["nombre"], dni=informacion["dni"],
                                    email=informacion["email"])
            cliente_crear.save()

            return redirect("/app/mostrar_clientes")

    return render(request, "App/agregar.html", contexto)


class AgregarProducto(LoginRequiredMixin,CreateView):
    template_name = "App/agregar.html"
    model = Producto
    form_class = ProductoForm
    success_url = "/app/productos"



@login_required
def mostrar_productos(request):
    productos = Producto.objects.all()
    contexto = {
        "productos": productos,
        "form": BuscarProductoForm,
    }
    return render(request, "App/mostrar_productos.html", contexto)

class DetalleProducto(LoginRequiredMixin,DetailView):
    model = Producto
    template_name = "App/detalle_producto.html"


@login_required
def agregar_venta_form(request):
    venta = VentaForm
    contexto = {
        "form": venta
    }

    if request.method == "POST":
        venta = VentaForm(request.POST)

        if venta.is_valid():
            informacion = venta.cleaned_data

            venta_crear = Venta(dni=informacion["dni"], nombre_producto=informacion["nombre_producto"],
                                cantidad_vendida=informacion["cantidad_vendida"])

            venta_crear.save()
            return redirect("/app/mostrar_ventas")

    return render(request, "App/agregar.html", contexto)

@login_required
def mostrar_ventas(request):
    ventas = Venta.objects.all()
    contexto = {
        "ventas": ventas,

    }
    return render(request, "App/mostrar_ventas.html", contexto)


def buscar_cliente(request):
    dni = request.GET["dni"]
    clientes = Cliente.objects.filter(dni__icontains=dni)

    contexto = {
        "clientes": clientes,
        "form": BuscarClienteForm,
    }
    return render(request, "App/mostrar_clientes.html", contexto)


def buscar_producto(request):
    titulo = request.GET["titulo"]
    productos = Producto.objects.filter(titulo__icontains=titulo)

    contexto = {
        "productos": productos,
        "form": BuscarProductoForm,
    }
    return render(request, "App/mostrar_productos.html", contexto)



class ProductoActualizacion(LoginRequiredMixin,UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = "/app/mostrar_productos"
    template_name = "App/agregar.html"

class ProductoEliminar(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Producto
    template_name = "App/eliminar_producto.html"
    success_url = "/app/mostrar_productos"

    def test_func(self):
        return self.request.user.is_staff


def about_me(request):
    contexto = {

    }
    return render(request, "app/about_me.html", contexto)

class Comentar(LoginRequiredMixin, CreateView):
    model = Comentarios
    form_class = ComentarioForm
    template_name = 'App/comentario.html'
    success_url = '/app/mostrar_productos'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.producto_id = self.kwargs['pk']
        return super(Comentar, self).form_valid(form)
