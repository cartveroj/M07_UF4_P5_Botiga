from django.db import models
from cataleg.models import Productes
from django.utils import timezone

'''Archivo que contiene los modelos de la aplicacion'''

class Carreto (models.Model):
    fecha_creacion = models.DateTimeField(default=timezone.now)
    productos = models.ManyToManyField(Productes, through='ProductoEnCarreto')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pagado = models.BooleanField(default=False)

class ProductoEnCarreto(models.Model):
    id_carreto = models.ForeignKey(Carreto, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productes, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
