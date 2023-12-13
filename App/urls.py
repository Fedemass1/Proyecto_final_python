from django.urls import path
from App.views import (show_html, agregar_cliente_form, mostrar_clientes,
                       AgregarProducto, mostrar_productos, agregar_venta_form,
                       mostrar_ventas, buscar_cliente, DetalleProducto, ProductoActualizacion, about_me,
                       ProductoEliminar, Comentar, buscar_producto, ComentarioEliminar)

urlpatterns = [
    path('show/', show_html),
    path('clientes/', agregar_cliente_form),
    path('mostrar_clientes/', mostrar_clientes),
    path('productos/', AgregarProducto.as_view(), name=''),
    path('mostrar_productos/', mostrar_productos),
    path('ventas/', agregar_venta_form),
    path('mostrar_ventas/', mostrar_ventas),
    path('buscar_cliente/', buscar_cliente),
    path('buscar_producto/', buscar_producto),
    path('producto/<int:pk>', DetalleProducto.as_view(), name="DetalleProducto"),
    path('editar_producto/<int:pk>', ProductoActualizacion.as_view(), name="ProductoEditar"),
    path('eliminar_producto/<int:pk>', ProductoEliminar.as_view(), name="ProductoEliminar"),
    path('producto/<int:pk>/comentario/', Comentar.as_view(), name='comentario'),
    path('comentario_eliminar/<int:pk>/', ComentarioEliminar.as_view(), name='ComentarioEliminar'),
    path('about_me/', about_me),


]
