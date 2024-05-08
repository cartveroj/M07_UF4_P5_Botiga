from rest_framework import serializers
from .models import Carreto, ProductoEnCarreto 

class ProductoEnCarretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoEnCarreto
        fields = ['id_producto','cantidad']



class CarretoSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Carreto
        fields = ['id', 'fecha_creacion','total','pagado']



