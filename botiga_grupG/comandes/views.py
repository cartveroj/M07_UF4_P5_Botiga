from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.db import transaction
from carreto.models import Carreto, ProductoEnCarreto
from .models import Comandes, CarretoEnComanda
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ComandesSerializer, CarretoEnComandesSerializer

'''Endpoint que recupera todas las comandas creadas en la base de datos'''
@api_view(['GET'])
def read_comandas(request):
     comandas = Comandes.objects.all()
     serializer = ComandesSerializer(comandas, many=True)
     return Response(serializer.data)

'''Endpoint que elimina una comanda'''
@api_view(['DELETE'])
def delete_comanda(request,pk):
    comanda = get_object_or_404(Comandes, pk=pk)
    comanda.delete()
    return Response({"message": "Comanda eliminado correctamente"}, status=200)

'''Endpoint que añade comanda a la base de datos'''
@api_view(['POST'])
def add_comanda(request):
    serializer = ComandesSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=200)
    else:
        return Response(status=400)
    


############################################
'''Endpoint que recupera los carritos relacionados con comanda'''
@api_view(['GET'])
def get_carritos_by_comanda(request):
    comanda = Comandes.objects.first() #recuperamos la primera comanda creada
    carritos_en_comanda = CarretoEnComanda.objects.filter(comanda=comanda) #recuperamos los carritos vinculados a una comanda
    carritos_con_productos_ids =  ProductoEnCarreto.objects.values('id_carreto').distinct() #recuperamos los carritos con productos
    carritos_sin_productos = carritos_en_comanda.exclude(carreto_id__in=carritos_con_productos_ids) #recuperamos los carritos sin productos
    
    # Eliminar los registros de CarretoEnComanda de todos los carritos 
    # que no contengan productos, porque solo queremos los que contengan productos
    with transaction.atomic():
        carritos_sin_productos.delete()

    #Serializamos los datos
    serializer_carritos_en_comanda = CarretoEnComandesSerializer(carritos_en_comanda, many=True)
    serializer_comanda = ComandesSerializer(comanda)
    #armamos el objeto y lo retornamos
    comanda_data = {
        'comanda': serializer_comanda.data,
        'carritos': serializer_carritos_en_comanda.data,
    }
    
    return Response(comanda_data)

'''Endpoint que recupera de la tabla relacion carretoEnComanda de todos
carritos que se encuentran pagados'''
@api_view(['GET'])
def get_historico_carritos(request):
    comanda = Comandes.objects.first()

    carritos_pagados = Carreto.objects.filter(pagado=True) #filtro de pagado
    carrito_comanda_pagados = CarretoEnComanda.objects.filter(carreto__in=carritos_pagados)

    serializer_carritos_pagados = CarretoEnComandesSerializer(carrito_comanda_pagados, many=True)
    serializer_comanda = ComandesSerializer(comanda)
    comanda_data = {
          'comanda': serializer_comanda.data,
          'carritos_pagados': serializer_carritos_pagados.data,
    }
     
    return Response(comanda_data)
'''Endpoint que retorna los carritos pendientes de pagar de la tabla relacional de carritosEnComanda'''
@api_view(['GET'])
def get_pendientes_carritos(request):
    comanda = Comandes.objects.first()
    carritos_pendientes = Carreto.objects.filter(pagado=False)#filtramos si esta pagado o no

    carrito_comanda_pendientes = CarretoEnComanda.objects.filter(carreto__in=carritos_pendientes)
    serializer_carritos_pendientes = CarretoEnComandesSerializer(carrito_comanda_pendientes, many=True)
    serializer_comanda = ComandesSerializer(comanda)
    
    comanda_data = {
          'comanda': serializer_comanda.data,
          'carritos_pendientes': serializer_carritos_pendientes.data,
    }
     
    return Response(comanda_data)