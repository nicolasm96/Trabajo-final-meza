from django.db import models

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto

# Create your models here.

