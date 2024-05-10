from rest_framework import serializers
from .models import Carreto, ProductoEnCarreto 

class ProductoEnCarretoSerializer(serializers.ModelSerializer):
    preu = serializers.ReadOnlyField(source='id_producto.preu')
    nom_producte = serializers.ReadOnlyField(source='id_producto.nom_producte')
    class Meta:
        model = ProductoEnCarreto
        fields = ['id_producto','preu','nom_producte','cantidad']



class CarretoSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Carreto
        fields = ['id', 'fecha_creacion','total','pagado']



