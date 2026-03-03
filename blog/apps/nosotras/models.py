from django.db import models

class SobreNosotras(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo

# Create your models here.
