from rest_framework import serializers
from .models import Carreto, ProductoEnCarreto 
from cataleg.serializers import ProductesCarretoSerializer
from cataleg.models import Productes

class ProductoEnCarretoSerializer(serializers.ModelSerializer):
   # producto = ProductesCarretoSerializer(read_only=True, many=True,)
    class Meta:
        model = ProductoEnCarreto
        fields = ['id_producto','cantidad']



class CarretoSerializer(serializers.ModelSerializer):
   #productos = ProductoEnCarretoSerializer(many=True, read_only=True)
    class Meta:
        
        model = Carreto
        fields = ['id','id_user', 'fecha_creacion','total','pagado','metodo_pago']



