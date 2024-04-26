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
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class ProductoEnCarreto(models.Model):
    tipo_pago =[
        ("paypal","paypal"),
        ("tarjeta","tarjeta"),
        ("transferencia","transferencia")
    ]
    id_carreto = models.ForeignKey(Carreto, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productes, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    metodo_pago = models.CharField(max_length=30, choices=tipo_pago)

def calcular_importe(self):
    return self.cantidad * self.id_producto.preu