from rest_framework import serializers
from .models import Carreto, ProductoEnCarreto


class CarretoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carreto
        fields = ['id_user', 'fecha_creacion']



class ProductoEnCarretoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductoEnCarreto
        fields = ['id_producto', 'id_carreto','cantidad', 'importe', 'metodo_pago']

