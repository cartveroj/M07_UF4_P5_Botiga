from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from carreto.models import Carreto

@api_view(['GET','POST'])
def paga_carreto(request, pk):
    carreto = Carreto.objects.get(id=pk)
    if carreto.pagado != True: #Controla que no sigui true el estat de pagat per tal de que si ja està pagat avisi.
        carreto.pagado = True
        carreto.save()
        return Response("Pagat")
    else :
        return Response("Aquest carreto ja està pagat")
