from django.shortcuts import render

# Create your views here.

#Vista basada en funcion
def funcion_hola(request):
    #que va a regresar un render con el mensaje
    return render(request, 'mensaje.html')

def mensaje(request):
    nombre = 'Eli'
    edad = 20
    context = {
        'nombre': 'Eli',
        'edad': 20,
        'materias':[
            'Frameworks',
            'Delployment',
            'administracion',
            'linux',
            'pruebas',
        ],
        'calificaciones':{
            'frameworks': 10,
            'algebra': 9,
            'requerimientos': 8,
        },
    }
    #return render(request, 'mensaje_variables.html', {'nombre': nombre, 'edad': edad})
    return render(request, 'mensaje_variables.html', context)

def materias(request):
    context = {
        'calificaciones':{'materia': 'Calidad de software', 'calificacion':8},
    }
    return render(request, 'mensaje_variables.html', context)

def mensajevar(request, edad, nombre):
    context = {
        'edad': edad,
        'nombre': nombre,
    }
    return render(request, 'mensaje_variables.html', context)

'''
[
    {'materia': 'Algebra', 'calificacion':10},
    {},

]

'''