from django.shortcuts import render
from AppBlog.views import obtener_avatar

def inicio(request):
    return render(request, 'blog_noticias/inicio.html', {'imagen':obtener_avatar(request)})

