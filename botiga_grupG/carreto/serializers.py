from rest_framework import serializers



class CarretoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['id_producto', 'cantidad', 'importe', 'metodo_pago']

