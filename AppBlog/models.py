from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now



# Perfil

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=400, blank=True)
    image = models.ImageField(upload_to ='perfil_image', default='icono-perfil-default.png')
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    def __str__(self):
        return f'Perfil de {self.user.username}'


# Noticias

class Publicacion(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publish_date = models.DateField(default=now)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='publicacion_imagen', blank = True, null = True)
    is_active = models.BooleanField(default=True, blank = True)

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'
    def __str__(self):
        return self.title
