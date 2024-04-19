from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


from .models import Carreto
from .serializers import CarretoSerializer

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
    
@api_view(['POST'])
def delete_carreto(request, carreto_id):
    if request.method == 'POST':
        carretoRecu = Carreto.objects.get(pk=carreto_id)
        if Carreto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            carretoRecu.delete()
            return Response(status=status.HTTP_200_OK)
       

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Carreto.objects.all()
    serializer_class = CarretoSerializer