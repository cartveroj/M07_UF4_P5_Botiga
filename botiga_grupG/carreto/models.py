from django.db import models
from enum import Enum
from cataleg.models import Productes
from pagaments.models import Usuari
from django.utils import timezone

# Create your models here.

class Carreto (models.Model):
    id_user = models.ForeignKey(Usuari, on_delete=models.CASCADE, default=1)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    productos = models.ManyToManyField(Productes, through='ProductoEnCarreto')

class ProductoEnCarreto(models.Model):
    tipo_pago =[
        ("paypal","paypal"),
        ("tarjeta","tarjeta"),
        ("transferencia","transferencia")
    ]
    id_carreto = models.ForeignKey(Carreto, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productes, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    importe = models.DecimalField(max_digits=5, decimal_places=3)
    metodo_pago = models.CharField(max_length=30, choices=tipo_pago)