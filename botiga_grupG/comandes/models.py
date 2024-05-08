from django.db import models
from carreto.models import Carreto

# Create your models here.
class Comandes(models.Model):
    id_carreto = models.ForeignKey(Carreto, on_delete=models.CASCADE)
    pagada = models.BooleanField()