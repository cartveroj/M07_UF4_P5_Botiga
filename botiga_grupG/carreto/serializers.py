from rest_framework import serializers
from models import Carreto

class CarretoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Carreto
        fields = ['id_producto', 'cantidad', 'importe', 'metodo_pago']

