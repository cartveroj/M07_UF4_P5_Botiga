from django.db import models
from carreto.models import Carreto

# Create your models here.
class Pagaments (models.Model):
    tipo_pago = [
        ("paypal", "paypal"),
        ("tarjeta", "tarjeta"),
        ("transferencia", "transferencia")
    ]
    metodo_pago = models.CharField(max_length=30, choices=tipo_pago, default="tarjeta")
    carreto = models.ForeignKey(Carreto,on_delete=models.CASCADE, default=None, null=True)
