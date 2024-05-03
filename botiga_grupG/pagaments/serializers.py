from .models import Pagaments
from rest_framework import serializers

class PagamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pagaments
        fields = []