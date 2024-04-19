from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Carreto
from .serializers import CarretoSerializer
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
        serializer = CarretoSerializer(data=request.data)
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

