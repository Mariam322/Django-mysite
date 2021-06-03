from django.shortcuts import render
from django.template import loader

def index3(request):
    return render(request,'accueil.html')
