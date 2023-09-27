from django.shortcuts import render
from django.urls import path

# Create your views here.
from .models import *

def home(request):
    return render(request, 'home.html')

def blog(request):
    content = {
        "maqolalalar": Maqola.objects.all()
    }
    return render(request, 'blog.html', content)

def about(request):
    content = {

    }

