from rest_framework import serializers
from .models import Comandes, CarretoEnComanda

class CarretoEnComandesSerializer(serializers.ModelSerializer):
    pagado = serializers.ReadOnlyField(source='carreto.pagado')
    class Meta:
        model = CarretoEnComanda
        fields = ['carreto','pagado']

class ComandesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comandes
        fields = ['id','fecha_creacion_comanda']
