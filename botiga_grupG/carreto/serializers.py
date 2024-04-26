from rest_framework import serializers
from .models import Carreto, ProductoEnCarreto


class CarretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreto
        fields = ['id','id_user', 'fecha_creacion','total']



class ProductoEnCarretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoEnCarreto
        fields = ['id_producto', 'id_carreto','cantidad', 'metodo_pago']

