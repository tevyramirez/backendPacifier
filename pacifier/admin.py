# admin.py
from django.contrib import admin
from .models import CategoriaProducto, SubcategoriaProducto, Producto, Cliente, PedidoVenta, DetallePedidoVenta, Empleado, Proveedor, PedidoCompra, DetallePedidoCompra, CreditoProveedor, DetallePagoProveedor

# Registra todos los modelos en el panel de administración
admin.site.register(CategoriaProducto)
admin.site.register(SubcategoriaProducto)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(PedidoVenta)
admin.site.register(DetallePedidoVenta)
admin.site.register(Empleado)
admin.site.register(Proveedor)
admin.site.register(PedidoCompra)
admin.site.register(DetallePedidoCompra)
admin.site.register(CreditoProveedor)
admin.site.register(DetallePagoProveedor)

