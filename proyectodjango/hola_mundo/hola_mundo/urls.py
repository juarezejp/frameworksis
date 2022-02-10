
from django.contrib import admin
from django.urls import path
from mensaje.views import funcion_hola

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', funcion_hola),

]
