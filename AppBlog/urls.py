from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
    path('', inicio, name='inicio'),
    path('aboutme', about_me, name='aboutme'),
    path('sign_up', sign_up, name='registrarse'),
    path('login', log_in, name='iniciar_sesion'),
    path('logout', logout_view, name='cerrar_sesion'),
    path('perfil', ver_perfil, name='mi_perfil'),
    path('actualizar_perfil/<int:pk>/', Update_profile.as_view(), name='editar_perfil'),
    path('todas_las_noticias/', Lista_noticias.as_view(), name='leer_noticias'),
    path('noticia/<int:pk>/', Noticia_detallada.as_view(), name= 'noticia'),
    path('noticia/nueva/', Crear_noticia.as_view(), name='crear_noticia'),
    path('noticia/borrar/<int:pk>/', Borrar_noticia.as_view(), name='borrar_noticia'),
    path('noticia/editar/<int:pk>/', Editar_noticia.as_view(), name='editar_noticia')
    
]