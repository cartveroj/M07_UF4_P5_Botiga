from django.db import models
from carreto.models import Carreto
from django.utils import timezone

'''Archivo que con tiene los modelos de la aplicacion
Comandas y carretoEnComando(que es cuando se tiene una carrito con productos)
'''
class Comandes(models.Model):
    fecha_creacion_comanda = models.DateTimeField(default=timezone.now)
    carritos = models.ManyToManyField(Carreto, through='CarretoEnComanda')


class CarretoEnComanda(models.Model):
    comanda = models.ForeignKey(Comandes, on_delete=models.CASCADE, default=None,null=True)
    carreto = models.ForeignKey(Carreto, on_delete=models.CASCADE,default=None, null=True)