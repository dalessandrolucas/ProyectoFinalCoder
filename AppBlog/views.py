from atexit import register
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.



def inicio(request):
    return render(request, 'inicio.html')

def about_me(request):
    return render(request, 'aboutme.html')

def log_in(request):
    if request.method == 'POST':
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=request.POST["username"]
            contraseña=request.POST["password"]
            usuario= authenticate(username=user, password=contraseña)
            if usuario is not None:
                login(request ,usuario)
                return render(request, 'sesion_iniciada.html', {'mensaje':f"Bienvenido de nuevo {usuario}!"})
            else:
                context = {'errores':'Tus datos son incorrectos!'}
                form = AuthenticationForm()
                return render(request, 'login.html', context = context)
        else:
            errores = form.errors
            form = AuthenticationForm()
            context = {'errores':errores, 'form':form} 
            return render(request, 'login.html', context = context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'login.html', context = context)


def sign_up(request):
    if request.method=='POST':
        form= Registrar_usuario(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            context = {'mensaje':f'Usuario creado correctamente, bienvenido {username}'}
            return render(request, 'usuario_creado.html', context = context)
        else:
         errores = form.errors
         form = Registrar_usuario()
         context = {'errores':errores, 'formulario':form}
         return render(request, 'sign_up.html', context = context)
    else:
      form = Registrar_usuario()
      context = {'formulario':form}
      return render(request, 'sign_up.html', context = context)
