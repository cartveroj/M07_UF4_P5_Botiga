from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Productes, Cataleg
from rest_framework import serializers
from .serializers import ProductesSerializer, CatalegSerializer
# Create your views here.

@api_view()
def api_cataleg (request):
    return Response({"message": "Benvingut a la API CATALEG"})



# G E T  P R O D U C T E S

@api_view()
def veure_productes(request):
    productes = Productes.objects.all()

    productes_json = ProductesSerializer(productes,many=True)

    return Response(productes_json.data)

# G E T  P R O D U C T E

@api_view()
def veure_producte(request,pk):
    productes = Productes.objects.get(id = pk)
    productes_json = ProductesSerializer(productes,many=False)

    return Response(productes_json.data)




# C R E A T E  D E  P R O D U C T E S
@api_view(['POST'])
def afegir_producte(request):
    producte = ProductesSerializer(data = request.data)

    if Productes.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Ja existeix aquest producte')

    if producte.is_valid():
        producte.save()
        return Response(producte.data)
    else:
        return Response("Ha fallat")


# U P D A T E  D E  P R O D U C T E S

@api_view(['POST'])
def actualitza_producte(request,pk):
    producte = Productes.objects.get(id=pk)
    serializer = ProductesSerializer(instance=producte, data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("No s'ha pogut actualitzar")


# D E L E T E  D E  P R O D U C T E

@api_view(['DELETE'])
def elimina_producte(request,pk):
    producte = Productes.objects.get(id=pk)
    producte.delete()
    return Response("Producte eliminat")

# G E T  D E  C A T A L E G

@api_view()
def veure_cataleg(request):
    cataleg = Cataleg.objects.all()
    cataleg_serializer = CatalegSerializer(cataleg, many=True, context={'request': request})
    return Response(cataleg_serializer.data)


# C R E A T E  D E  C A T A L E G

@api_view(['POST'])
def afegeix_producte_cataleg(request):

    producte_id = request.data.get('producte_id') #Obtenim la id del producte del body de la solicitut que fem


    producte = Productes.objects.get(id=producte_id) #Busca el producte amb la id proporcionada
    if not producte :
        return Response("No existeix el producte amb aquesta id")

    cataleg_amb_id = Cataleg.objects.filter(producte_id = producte_id).first()
    if  cataleg_amb_id:
        return Response("Ja existeix un cataleg amb aquesta id")
    else :
        cataleg = Cataleg(producte=producte) #Crea una instància nova de Catàleg amb el producte
        cataleg.save()

        serializer = CatalegSerializer(cataleg) #Obtenim la instancia del cataleg amb el producte afegit ja serialitzat
        return Response(serializer.data)

# D E L E T E  D E  C A T A L E G

@api_view(['DELETE'])
def elimina_producte_cataleg(request,pk):
    producte_cataleg = Cataleg.objects.get(id=pk)
    producte_cataleg.delete()
    return Response("Eliminat producte del catàleg")

