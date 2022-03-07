from django.urls import path
from articulos import views


urlpatterns = [
    path('', views.lista_articulos, name='articulos_lista'),
    path('nuevo', views.nuevo_articulo, name='nuevo_articulo'),
    path('eliminar/<int:id>', views.eliminar_articulos, name='eliminar_articulos'),
    path('editar/<int:id>', views.editar_articulos, name='editar_articulos'),
    path('listacategoria', views.lista_categoria, name='categoria_lista'),
    path('nuevacategoria', views.nueva_categoria, name='nueva_categoria'),
    path('eliminarcategoria/<int:id>', views.eliminar_categoria, name='eliminar_categoria'),
    path('editarcategoria/<int:id>', views.editar_categoria, name='editar_categoria'),
]
