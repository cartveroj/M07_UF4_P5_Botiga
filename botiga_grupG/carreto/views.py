from datetime import date, timezone
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Carreto
from cataleg.models import Productes
from pagaments.models import Usuari

from .models import ProductoEnCarreto
from .serializers import CarretoSerializer, ProductoEnCarretoSerializer
from rest_framework import status


# Create your views here.

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view(['GET'])
def read_carreto(request):
    queryset = Carreto.objects.all()
    serializer = CarretoSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_carreto(request):
    if request.method == 'POST':
        producto_id = request.data.get('id_producto')
        cantidad = request.data.get('cantidad')
        metodo = request.data.get('metodo_pago')
        
        #de momento solo usuario 1
        usuario = Usuari.objects.get(pk=2)
        carrito,created = Carreto.objects.get_or_create(id_user=usuario ,fecha_creacion = date.today())
        firstCarrito = Carreto.objects.first()

        productoRec = Productes.objects.get(pk=producto_id)
        ProductoCarreto = ProductoEnCarreto.objects.create(
            id_producto = productoRec.id,
            id_carreto = firstCarrito.id, 
            cantidad = int(cantidad),
            importe = (cantidad * productoRec.preu),
            metodo_pago = metodo
        )
        ProductoCarreto.save()
        serializer = ProductoEnCarretoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['PUT'])
def update_carreto(request, pk):
    try:
        carrito = Carreto.objects.get(pk=pk)
    except Carreto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    nueva_cantidad = request.data.get('nueva_cantidad')
    carrito.cantidad = nueva_cantidad
    carrito.save()

    serializer = CarretoSerializer(carrito)
    return Response(serializer.data)

