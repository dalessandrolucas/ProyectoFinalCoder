from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
    path('', inicio, name='inicio'),
    path('aboutme', about_me, name='aboutme'),
    path('sign_up', sign_up, name='registrarse'),
    path('login', log_in, name='iniciar_sesion'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout')
    
]