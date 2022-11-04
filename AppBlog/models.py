from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now




# Noticias

class Publicacion(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publish_date = models.DateField(default=now)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='publicacion_imagen', blank = True, null = True)

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'
    def __str__(self):
        return self.author+","+self.title


class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)