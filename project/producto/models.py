from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300, null=True, blank=True, verbose_name="descripcion")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.FloatField()
    talle = models.CharField(max_length=10,  null=True, blank=True, verbose_name="talle")

    def __str__(self):
        return self.nombre


# Create your models here.
