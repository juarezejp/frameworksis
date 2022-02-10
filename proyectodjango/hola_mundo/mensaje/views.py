from django.shortcuts import render

# Create your views here.

def funcion_hola(request):
    #que va a regresar un render con el mensaje
    return render(request, 'mensaje.html')