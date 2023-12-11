from django.contrib import admin

from App.models import Cliente, Producto, Venta

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Venta)