from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.



def inicio(request):
    return render(request, 'inicio.html')

def about_me(request):
    return render(request, 'aboutme.html')