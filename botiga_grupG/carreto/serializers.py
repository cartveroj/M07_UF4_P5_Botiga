from rest_framework import serializers
from .models import Carreto, ProductoEnCarreto 

'''Clases que serializan los modelos de productoEnCarreto y Carreto'''
class ProductoEnCarretoSerializer(serializers.ModelSerializer):
    #Visualizamos los campos de la tabla productes de modo solo lectura
    preu = serializers.ReadOnlyField(source='id_producto.preu')
    nom_producte = serializers.ReadOnlyField(source='id_producto.nom_producte')
    class Meta:
        model = ProductoEnCarreto
        fields = ['id_producto','preu','nom_producte','cantidad']

class CarretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreto
        fields = ['id', 'fecha_creacion','total','pagado']



