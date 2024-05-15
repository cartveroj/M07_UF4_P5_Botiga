from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import ProductoEnCarreto
from .models import Carreto
from cataleg.models import Productes
from comandes.models import Comandes, CarretoEnComanda

from .serializers import CarretoSerializer, ProductoEnCarretoSerializer



# Create your views here.

##END POINTS DE CARRETOS

'''Endpoint que recupera datos de la tabla de carreto de la base de datos'''

@api_view(['GET'])
def read_carreto(request):
    queryset = Carreto.objects.all()
    serializer = CarretoSerializer(queryset, many=True)
    return Response(serializer.data)
'''Endpoint que añade registros de carreto a la tabla de carreto '''
@api_view(['POST'])
def add_carreto(request):
    serializer = CarretoSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=200) #retorna un 200 si todo fue bien
    else:
        return Response(status=400)

'''Endpoint que elimina carritos de la tabla, recibe la id por parametros y elimina por id'''
@api_view(['DELETE'])
def delete_carreto(request,pk):
    carrito = get_object_or_404(Carreto, pk=pk) #si no encuentra retorna un error 404
    carrito.delete()
    return Response({"message": "Carrito eliminado correctamente"}, status=200)

    

#END POINTS DE PRODUCTOS EN CARRETO

'''Endpoint metodo GET que recupera de la tabla de relación de productos y tabla, que se llama
productos en carrito'''
@api_view(['GET'])
def get_productos_by_carrito(request):
    carritos = Carreto.objects.filter(pagado=False) #filtramos que no este pagado
    carritos_con_productos = []

    for carrito in carritos:
        productos_en_carrito = ProductoEnCarreto.objects.filter(id_carreto=carrito)
        serializer_productos = ProductoEnCarretoSerializer(productos_en_carrito, many=True)
        
        carrito_data = {
            'carreto': CarretoSerializer(carrito).data,
            'productos': serializer_productos.data
        }
        #Añadimos al arrar el objeto de relacion de carreto con productos
        carritos_con_productos.append(carrito_data)

    return Response(carritos_con_productos)

'''Endpoint metodo POST es el que se encarga de hacer la relacion de carrito-producto
en la tabla ProductosEnCarreto'''
@api_view(['POST'])
def add_productos_al_carreto(request):

    if request.method == 'POST':
        #recuperamos la comanda si existe o sino la creamos
        comanda, _ = Comandes.objects.get_or_create() #si no existe una comanda creada lo crea 
        #recuperamos los datos enviados en el request
        producto_id = request.data.get('id_producto')
        cantidad = request.data.get('cantidad')
        carrito_id = request.data.get('id_carreto')

        carrito = Carreto.objects.get(pk=carrito_id)
       
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
        #añadimos en la tabla carritoEnComanda 
        if not CarretoEnComanda.objects.filter(comanda = comanda,carreto_id=carrito_id).exists():
           CarretoEnComanda.objects.create(comanda=comanda, carreto=carrito) #añadimos la relacion de carrito comanda

        #serializamos el resultado 
        serializer = ProductoEnCarretoSerializer(producto_en_carrito)
        return Response(serializer.data, status=200 if not created else 201)

'''Endpoint que elimina los productos de la tabla relacional productosEnCarreto
enviamos por parametro al id del carrito y la id del producto a eliminar'''           
@api_view(['DELETE'])
def eliminar_productos_carreto(request, carreto_id, producto_id):
    #Filtramos si existe el producto en el carrito
    productos_en_carrito = ProductoEnCarreto.objects.filter(id_carreto_id= carreto_id, id_producto_id=producto_id).first() 
    #si existe modificamos el total del carrito
    if productos_en_carrito:
       importe = productos_en_carrito.cantidad *  Productes.objects.get(pk=producto_id).preu
       carrito = Carreto.objects.get(pk=carreto_id)
       carrito.total -= importe
       carrito.save()
    #eliminamos
       productos_en_carrito.delete()

       return Response({'message': 'Producto eliminado del carrito.'}, status=200)
    else:
        return Response({'error': 'Producto no encontrado en el carrito.'}, status=404)
    
'''Endpoint que modifica la cantidad del producto '''
@api_view(['PUT'])
def update_cantidad_producto_carreto(request):
    producto_id =  request.data.get('id_producto')
    carreto_id = request.data.get('id_carreto')
    nueva_cantidad = request.data.get('nueva_cantidad')

    #Verificamos que este en el carrito
    try:
        producto_en_carrito = ProductoEnCarreto.objects.get(id_carreto_id=carreto_id, id_producto_id=producto_id)
    except ProductoEnCarreto.DoesNotExist:
        return Response({'error': 'Producto no encontrado en el carrito.'}, status=404)
    #si existe modificamos la cantidad nueva
    producto_en_carrito.cantidad = nueva_cantidad
    producto_en_carrito.save()

    # Obtener todos los productos en el carrito
    productos_en_carrito = ProductoEnCarreto.objects.filter(id_carreto_id=carreto_id)

    # Recalcular el importe total del carrito y si tiene mas productos
    importe_total = 0
    for producto_en_carrito in productos_en_carrito:
        importe_total += producto_en_carrito.cantidad * producto_en_carrito.id_producto.preu

    carrito = Carreto.objects.get(pk=carreto_id)
    carrito.total = importe_total
    carrito.save()

    serializer = ProductoEnCarretoSerializer(producto_en_carrito)
    return Response(serializer.data, status=200)
   

