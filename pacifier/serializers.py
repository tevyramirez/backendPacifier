from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class DetallePedidoVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedidoVenta
        fields = '__all__'

class PedidoVentaSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoVentaSerializer(many=True, read_only=True)

    class Meta:
        model = PedidoVenta
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

