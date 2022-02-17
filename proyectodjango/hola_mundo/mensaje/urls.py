from django.urls import path
from mensaje import views

urlpatterns = [
    path('', views.funcion_hola), #hola
    path('mensaje', views.mensaje),#hola/mensaje
    #path('mensaje/<\d+>', views.mensaje),# con numero
    #path('mensaje/<\w+>', views.mensaje),# con letras
    path('mensaje/<int:edad>/<str:nombre>', views.mensajevar),#espera una variable edad
    path('materias', views.materias),

]

