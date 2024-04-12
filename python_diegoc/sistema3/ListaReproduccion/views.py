from django.shortcuts import render
from django.http import HttpResponse
from .models import Cancion

def inicio(request):
    lista_canciones = Cancion.objects.all()
    return render(request,"index.html",{"canciones":lista_canciones})

