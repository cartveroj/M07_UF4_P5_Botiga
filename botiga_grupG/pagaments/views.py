from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from carreto.models import Carreto

@api_view(['GET','POST'])
def paga_carreto(request, pk):
    carreto = Carreto.objects.get(id=pk)
    if carreto.pagado != True:
        carreto.pagado = True
        carreto.save()
        return Response("Pagat")
