from django.db import models

# Create your models here.
class Pagaments (models.Model):
    num_tarjeta = models.CharField(max_length=50)
    ccv = models.CharField(max_length=3)
    caducitat = models.DateTimeField()

class Usuari (models.Model):
    nom_usuari = models.CharField(max_length=50)
    contrassenya = models.CharField(max_length=50)
    id_tarjeta = models.ForeignKey(Pagaments,on_delete=models.CASCADE)