from datetime import date, timezone
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Carreto
from cataleg.models import Productes
from django.shortcuts import get_object_or_404

from .models import ProductoEnCarreto
from .serializers import CarretoSerializer, ProductoEnCarretoSerializer
from rest_framework import status


# Create your views here.

##END POINTS DE CARRETOS

@api_view(['GET'])
def read_carreto(request):
    queryset = Carreto.objects.all()
    serializer = CarretoSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_carreto(request):
    serializer = CarretoSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        carrito = serializer.save()
        return Response(serializer.data,status=200)
    else:
        return Response(status=400)

@api_view(['DELETE'])
def delete_carreto(request,pk):
    carrito = get_object_or_404(Carreto, pk=pk)
    carrito.delete()
    return Response({"message": "Carrito eliminado correctamente"}, status=200)

# @api_view(['PUT'])
# def update_carreto(request,pk):
#     carrito = get_object_or_404(Carreto, pk=pk)
#     carrito.delete()
#     return Response({"message": "Carrito eliminado correctamente"}, status=200)

#END POINTS DE PRODUCTOS EN CARRETO

@api_view(['GET'])
def get_productos_by_carrito(request):
    carritos = Carreto.objects.all()
    carritos_con_productos = []

    for carrito in carritos:
        productos_en_carrito = ProductoEnCarreto.objects.filter(id_carreto=carrito)
        serializer_productos = ProductoEnCarretoSerializer(productos_en_carrito, many=True)

        carrito_data = {
            'carreto': CarretoSerializer(carrito).data,
            'productos': serializer_productos.data
        }
        carritos_con_productos.append(carrito_data)

    return Response(carritos_con_productos)

@api_view(['POST'])
def add_productos_al_carreto(request):
    if request.method == 'POST':
        producto_id = request.data.get('id_producto')
        cantidad = request.data.get('cantidad')
        carrito_id = request.data.get('id_carreto')
        #de momento solo usuario 2
        #usuario = Usuari.objects.get(pk=2)

        carrito = Carreto.objects.get(pk=carrito_id)
        # except Carreto.DoesNotExist:
        #     carrito = Carreto.objects.create(id_user=usuario, fecha_creacion=date.today())

        # Verifica si el producto ya está en el carrito
        producto_en_carrito, created = ProductoEnCarreto.objects.get_or_create(
            id_carreto_id=carrito_id,
            id_producto_id=producto_id,
            defaults={
                'cantidad': int(cantidad),
            }
        )

        if not created:
            # Si el producto ya está en el carrito, actualiza la cantidad
            producto_en_carrito.cantidad += int(cantidad)
            producto_en_carrito.save()

        # Actualiza el total del carrito
        importe = int(cantidad) * Productes.objects.get(pk=producto_id).preu
        carrito.total += importe
        carrito.save()

        serializer = ProductoEnCarretoSerializer(producto_en_carrito)
        return Response(serializer.data, status=200 if not created else 201)

@api_view(['POST'])
def eliminar_productos_carreto(request):
    producto_id = request.data.get('id_producto')
    carreto_id = request.data.get('id_carreto')

    productos_en_carrito = ProductoEnCarreto.objects.filter(id_carreto_id= carreto_id, id_producto_id=producto_id).first()
    if productos_en_carrito:
       importe = productos_en_carrito.cantidad *  Productes.objects.get(pk=producto_id).preu
       carrito = Carreto.objects.get(pk=carreto_id)
       carrito.total -= importe
       carrito.save()

       productos_en_carrito.delete()

       return Response({'message': 'Producto eliminado del carrito.'}, status=200)
    else:
        return Response({'error': 'Producto no encontrado en el carrito.'}, status=404)


@api_view(['PUT'])
def update_producto_carreto(request):
    producto_id =  request.data.get('id_producto')
    carreto_id = request.data.get('id_carreto')
    nueva_cantidad = request.data.get('nueva_cantidad')

    try:
        productos_en_carrito = ProductoEnCarreto.objects.filter(id_carreto_id= carreto_id, id_producto_id=producto_id).first()
    except ProductoEnCarreto.DoesNotExist:
        return Response({'error': 'Producto no encontrado en el carrito.'}, status=404)

    productos_en_carrito.cantidad = nueva_cantidad
    productos_en_carrito.save()

    # Recalcular el importe total del carrito
    importe = productos_en_carrito.cantidad *  Productes.objects.get(pk=producto_id).preu
    carrito = Carreto.objects.get(pk=carreto_id)
    carrito.total = importe
    carrito.save()

    serializer = ProductoEnCarretoSerializer(productos_en_carrito)
    return Response(serializer.data, status=200)


