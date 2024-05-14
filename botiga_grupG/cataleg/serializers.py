from .models import Cataleg, Productes
from rest_framework import serializers

#Fem servir els serializers per tal de converir les instàncies dels models en tipus de python per a ser renderitzats a JSON
class CatalegSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cataleg
        fields = ['id','producte_id']

class ProductesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productes
        fields = ['id','nom_producte','preu','origen','pes_kg','stock','tipus_producte'] #Aqui indiquem els camps que necessitem
