from .models import Pagaments, Usuari
from rest_framework import serializers

class PagamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pagaments
        fields = ['num_tarjeta','ccv','caducitat']

class UsuariSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Usuari
        fields = ['nom_usuari','contrassenya','id_tarjeta_id']