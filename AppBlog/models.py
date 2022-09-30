from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to ='profile_image', default='icono_proyecto.png')
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    def __str__(self):
        return f'Perfil de {self.user.username}'

