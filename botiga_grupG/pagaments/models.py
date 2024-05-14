from django.db import models
from carreto.models import Carreto

# Degut al canvi en el fluxe de dades i el model entitat relació aquest model no entra en joc en la api, la idea era que un usuari pogués escollir el metode de pagament
class Pagaments (models.Model):
    tipo_pago = [
        ("paypal", "paypal"),
        ("tarjeta", "tarjeta"),
        ("transferencia", "transferencia")
    ]
    metodo_pago = models.CharField(max_length=30, choices=tipo_pago, default="tarjeta")
    carreto = models.ForeignKey(Carreto,on_delete=models.CASCADE, default=None)
