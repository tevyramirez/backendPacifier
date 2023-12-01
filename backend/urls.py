from django.urls import path
from django.contrib import admin
from pacifier.views import *
from django.urls import path

urlpatterns = [
     path('admin/', admin.site.urls),
    path('api/productos/', ListarProductos.as_view(), name='listar_productos'),
    path('api/productos/crear/', CrearProducto.as_view(), name='crear_producto'),
    path('api/productos/<int:pk>/', DetalleProducto.as_view(), name='detalle_producto'),
     path('api/productos/<int:pk>/', ActualizarProductoAPIView.as_view(), name='actualizar_producto_api'),
     path('api/productos/<int:pk>/eliminar/', EliminarProductoAPIView.as_view(), name='eliminar_producto_api'),
    path('api/venta/', RealizarVenta.as_view(), name='realizar_venta'),
    path('api/clientes/', ListarClientes.as_view(), name='listar_clientes'),
    path('api/clientes/crear/', ClienteCreateView.as_view(), name='cliente-create'),
    path('api/clientes/eliminar/<int:id>/', ClienteDeleteView.as_view(), name='delete_user'),
    path('api/inventario/<int:pk>/', GestionarInventario.as_view(), name='gestionar_inventario'),
    path('api/login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('api/get_logged_in_user/', get_logged_in_user, name='get_logged_in_user'),
]
