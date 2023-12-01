from django.db import models
from django.contrib.auth.models import AbstractUser

class Empleado(models.Model):
    codigo = models.CharField(max_length=25)
    ci = models.CharField(max_length=13)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    email = models.EmailField()
    fecha_ingreso = models.DateField()
    estado_civil = models.CharField(max_length=10)
    login = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)
    modulo = models.CharField(max_length=100)

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

class SubcategoriaProducto(models.Model):
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    subcategoria = models.CharField(max_length=255)
    codigo = models.CharField(max_length=125)
    descripcion = models.TextField()

class Producto(models.Model):
    subcategoria = models.ForeignKey(SubcategoriaProducto, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=255)
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=10)
    stock = models.IntegerField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    ganancia = models.IntegerField()
    valor_ganancia = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    val_iva = models.DecimalField(max_digits=10, decimal_places=2)
    precio_iva = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    observacion = models.TextField()

class Cliente(models.Model):
    razon_social = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    observacion = models.TextField(null=True, blank=True)

class PedidoVenta(models.Model):
    fecha_compra = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total_descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total_iva = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_pago = models.CharField(max_length=10)
    efectivo = models.DecimalField(max_digits=10, decimal_places=2)
    deuda = models.DecimalField(max_digits=10, decimal_places=2)

class DetallePedidoVenta(models.Model):
    pedido_venta = models.ForeignKey(PedidoVenta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    unidad = models.CharField(max_length=10)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.IntegerField()
    valor_descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)


class Proveedor(models.Model):
    codigo = models.CharField(max_length=25)
    razon_social = models.CharField(max_length=255)
    representante = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    email = models.EmailField()
    dias_credito = models.IntegerField()
    fecha_ingreso = models.DateField()
    observacion = models.TextField()

class PedidoCompra(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    factura = models.CharField(max_length=20)
    fecha_compra = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total_descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total_iva = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_pago = models.CharField(max_length=10)
    efectivo = models.DecimalField(max_digits=10, decimal_places=2)
    deuda = models.DecimalField(max_digits=10, decimal_places=2)

class DetallePedidoCompra(models.Model):
    codigo = models.CharField(max_length=25)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_compra = models.ForeignKey(PedidoCompra, on_delete=models.CASCADE)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    unidad = models.CharField(max_length=10)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.IntegerField()
    valor_descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class CreditoProveedor(models.Model):
    cab_pedido_compra = models.ForeignKey(PedidoCompra, on_delete=models.CASCADE)
    comprobante = models.CharField(max_length=100)
    proveedor = models.CharField(max_length=255)
    fecha_compra = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento1 = models.DateField()
    cuota1 = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento2 = models.DateField()
    cuota2 = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento3 = models.DateField()
    cuota3 = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento4 = models.DateField()
    cuota4 = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento5 = models.DateField()
    cuota5 = models.DecimalField(max_digits=10, decimal_places=2)
    observacion = models.TextField()

class DetallePagoProveedor(models.Model):
    credito_proveedor = models.ForeignKey(CreditoProveedor, on_delete=models.CASCADE)
    factura = models.CharField(max_length=255)
    cuota = models.IntegerField()
    fecha_pago = models.DateTimeField()
    abono = models.DecimalField(max_digits=10, decimal_places=2)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    observacion = models.TextField(null=True, blank=True)

