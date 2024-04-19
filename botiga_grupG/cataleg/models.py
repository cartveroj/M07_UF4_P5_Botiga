from django.db import models

# Create your models here.

#Primer creem el model Producte ja que Cataleg necessitara la fk
class Productes (models.Model):

    TIPUS = [
        ('C','Carnics'),
        ('L','Làctics'),
        ('P','Peixos'),
        ('V','Verdures'),
        ('H','Hortalises'),
        ('F','Fruita'),
        ('FS','Fruits secs')
    ]
    nom_producte = models.CharField(max_length=50)
    preu = models.DecimalField(max_digits=5,decimal_places=2) #Posem el preu en decimal
    origen = models.CharField(max_length=50)
    pes_kg = models.DecimalField(max_digits=5,decimal_places=2)
    stock = models.IntegerField()
    tipus_producte = models.CharField(max_length=50,choices=TIPUS)

#Ara creem el model de Catàleg

class Cataleg (models.Model):
    producte = models.ForeignKey(Productes, on_delete=models.CASCADE)