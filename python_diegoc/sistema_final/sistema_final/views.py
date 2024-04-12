from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def formulario(request):

    plantilla = loader.get_template('form.html')
    documento = plantilla.render()
    return HttpResponse(documento)

