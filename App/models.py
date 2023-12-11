from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    dni = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return (f"Nombre del cliente: {self.nombre} -DNI del cliente: {self.dni} - "
                f"Correo electrónico del cliente: {self.email}")


class Producto(models.Model):
    id_producto = models.CharField(max_length=10, unique=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(default=datetime.now)
    imagen = models.ImageField(upload_to='producto')
    precio_venta = models.IntegerField()

    def __str__(self):
        return f"Producto: {self.titulo} - Precio de venta: {self.precio_venta}"


class Comentarios(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(default=datetime.now)


class Venta(models.Model):
    dni = models.CharField(max_length=10)
    nombre_producto = models.CharField(max_length=50)
    cantidad_vendida = models.IntegerField()

    def __str__(self):
        return (f"DNI del vendedor: {self.dni} - Producto vendido: {self.nombre_producto} - "
                f"Cantidad vendida: {self.cantidad_vendida}")
