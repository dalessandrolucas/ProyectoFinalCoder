from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Publicacion
from ckeditor.widgets import CKEditorWidget


class Registrar_usuario(UserCreationForm):
    username= forms.CharField(max_length=50)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)

class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}


class Editar_usuario(UserCreationForm): 
    email = forms.EmailField(label="Modificar Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')
    description=forms.CharField(label='Acerca de ti')
    class Meta:
        model = User
        fields = [ "email", "password1", "password2", 'first_name', 'last_name' ]
        help_text = {k:"" for k in fields}

class Noticia_formulario(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = '__all__'

class Agregar_avatar(forms.Form):
     imagen= forms.ImageField(label="Imagen")