from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Producto, Cliente, PedidoVenta
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status


"""Producto CRUD VIEWS"""
class ListarProductos(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class CrearProducto(generics.CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ActualizarProductoAPIView(generics.RetrieveUpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

class EliminarProductoAPIView(generics.DestroyAPIView):
    queryset = Producto.objects.all()
    permission_classes = [IsAuthenticated] 

class DetalleProducto(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class GestionarInventario(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

""" Cliente CRUD Views """

class ListarClientes(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteDeleteView(APIView):
    #Funcion para eliminar un usuario
    def delete(self, request, id):
        try:
          user = Cliente.objects.get(id=id)
          user.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
          return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

""" AUTH VIEWS """

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk, 'username': user.username},
                        status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_logged_in_user(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

""" VENTAS VIEWS """

class RealizarVenta(generics.CreateAPIView):
    queryset = PedidoVenta.objects.all()
    serializer_class = PedidoVentaSerializer
