from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Productes
from rest_framework import serializers
from .serializers import ProductesSerializer
# Create your views here.

@api_view()
def hello_world(request):
    return Response({"message": "Hello world!"})



# G E T  P R O D U C T E S

@api_view()
def veure_productes(request):
    productes = Productes.objects.all()

    productes_json = ProductesSerializer(productes,many=True)

    return Response(productes_json.data)

# G E T  P R O D U C T E

@api_view()
def veure_producte(request,pk):
    productes = Productes.objects.get(id = pk)
    productes_json = ProductesSerializer(productes,many=False)

    return Response(productes_json.data)




# C R E A T E  D E  P R O D U C T E S
@api_view(['POST'])
def afegir_producte(request):
    producte = ProductesSerializer(data = request.data)

    if Productes.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Ja existeix aquest producte')

    if producte.is_valid():
        producte.save()
        return Response(producte.data)
    else:
        return Response("Ha fallat")


# U P D A T E  D E  P R O D U C T E S

@api_view(['POST'])
def actualitza_producte(request,pk):
    producte = Productes.objects.get(id=pk)
    serializer = ProductesSerializer(instance=producte, data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("No s'ha pogut actualitzar")


# D E L E T E  D E  P R O D U C T E

@api_view(['DELETE'])
def elimina_producte(request,pk):
    producte = Productes.objects.get(id=pk)
    producte.delete()
    return Response("Producte eliminat")