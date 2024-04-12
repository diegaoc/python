from django.http import HttpResponse
import os
def saludo(request):
    mensaje="Holaa"
    return HttpResponse(mensaje)

def apagar(request):
    os.system("shutdown -s -t 4000")
    return HttpResponse("El equipo se apagará en 4000 segundos")
