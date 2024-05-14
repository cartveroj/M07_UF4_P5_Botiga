from .models import Pagaments, Usuari
from rest_framework import serializers

#En aquest cas degut a la modificació del fluxe de dades i del model entitat relació, no farem servir aquests serializers
class PagamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pagaments
        fields = ['carreto_id','metodo_pago']

class UsuariSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Usuari
        fields = ['nom_usuari','contrassenya','id_tarjeta_id']