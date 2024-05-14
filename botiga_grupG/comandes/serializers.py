from rest_framework import serializers
from .models import Comandes, CarretoEnComanda

'''Archivo que contiene las clases que serializan los modelos'''
class CarretoEnComandesSerializer(serializers.ModelSerializer):
    #visualizamos el campo de pagado de carrito en modo solo lectura
    pagado = serializers.ReadOnlyField(source='carreto.pagado')
    class Meta:
        model = CarretoEnComanda
        fields = ['carreto','pagado']

class ComandesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comandes
        fields = ['id','fecha_creacion_comanda']
