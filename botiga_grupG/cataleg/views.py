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
