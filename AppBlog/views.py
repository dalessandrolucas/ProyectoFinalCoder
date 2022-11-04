# Imports login-sign_up-logout
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib.auth.decorators import login_required


# Imports Perfil y Blog
from .models import Publicacion, Avatar
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView, ListView
from django.urls import reverse



def inicio(request):
    return render(request, 'blog_noticias/inicio.html', {'imagen':obtener_avatar(request)})

def about_me(request):
    return render(request, 'blog_noticias/aboutme.html', {'imagen':obtener_avatar(request)})

# Modulo login

def log_in(request):
    if request.method == 'POST':
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=request.POST["username"]
            contraseña=request.POST["password"]
            usuario= authenticate(username=user, password=contraseña)
            if usuario is not None:
                login(request ,usuario)
                return render(request, 'cuentas/sesion_iniciada.html', {'mensaje':f"Bienvenido de nuevo {usuario}!"})
            else:
                context = {'errores':'Tus datos son incorrectos!'}
                form = AuthenticationForm()
                return render(request, 'cuentas/login.html', context = context)
        else:
            errores = form.errors
            form = AuthenticationForm()
            context = {'errores':errores, 'form':form} 
            return render(request, 'cuentas/login.html', context = context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'cuentas/login.html', context = context)


def sign_up(request):
    if request.method=='POST':
        form= Registrar_usuario(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            context = {'mensaje':f'Usuario creado correctamente, bienvenido {username}'}
            return render(request, 'cuentas/usuario_creado.html', context = context)
        else:
         errores = form.errors
         form = Registrar_usuario()
         context = {'errores':errores, 'formulario':form}
         return render(request, 'cuentas/sign_up.html', context = context)
    else:
      form = Registrar_usuario()
      context = {'formulario':form}
      return render(request, 'cuentas/sign_up.html', context = context)

def logout_view(request):
    logout(request)
    return redirect('/blog')

# Perfil

@login_required
def ver_perfil(request):
    return render(request, 'cuentas/perfil.html')

@login_required 
def editarperfil(request):
    usuario = request.user
    if request.method=="POST":
        form=Editar_usuario(request.POST)
        if form.is_valid():
            
            usuario.first_name=form.cleaned_data["first_name"]
            usuario.last_name=form.cleaned_data["last_name"]
            usuario.email=form.cleaned_data["email"]
            usuario.password1=form.cleaned_data["password1"]
            usuario.password2=form.cleaned_data["password2"]
            usuario.save()
            return render(request, "cuentas/perfil.html", {"mensaje":f"editado con éxito "} )
    else:
        form= Editar_usuario(instance=usuario)
        return render(request, "cuentas/editar_perfil.html", {"form":form, "usuario":usuario})

@login_required
def obtener_avatar(request):
    lista= Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen=""
    return imagen

@login_required
def agregaravatar(request):
    if request.method == 'POST':
        form=Agregar_avatar(request.POST, request.FILES)
        if form.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)>0):
                avatarViejo.delete()
            avatar=Avatar(user=request.user, imagen=form.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'cuentas/agregar_avatar.html', {'usuario':request.user, "formulario":form, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE', "imagen":obtener_avatar(request)})
    else:
        form=Agregar_avatar()
    return render(request, 'cuentas/agregar_avatar.html', {'formulario':form, 'usuario':request.user, "imagen":obtener_avatar(request)})

@login_required
def borrarAvatar(request):
    avatar=Avatar.objects.filter(user=request.user)
    avatar.delete()
    formavatar=Agregar_avatar()
    return render(request, 'cuentas/agregar_avatar.html', {"formavatar":formavatar, "message":"Avatar eliminado", "imagen":obtener_avatar(request)})

# Blog/Noticias CRUD

class Crear_noticia(LoginRequiredMixin, CreateView):
    model = Publicacion
    template_name = 'blog_noticias/publicar_noticia.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('leer_noticias', kwargs={'pk':self.object.pk})

class Noticia_detallada(DetailView):
    model = Publicacion
    template_name = 'blog_noticias/noticia_detallada.html'

class Borrar_noticia(LoginRequiredMixin, DeleteView):
    model = Publicacion
    template_name = 'blog_noticias/borrar.html'
    def get_success_url(self):
        return reverse('leer_noticias')

class Editar_noticia(LoginRequiredMixin, UpdateView):
    model = Publicacion
    template_name = 'blog_noticias/editar_noticia.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('leer_noticias', kwargs = {'pk':self.object.pk})

class Lista_noticias(ListView):
    model = Publicacion
    template_name = 'blog_noticias/lista_noticias.html'
    queryset = Publicacion.objects.all()