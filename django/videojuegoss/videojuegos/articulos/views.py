from django.shortcuts import render, redirect
from django.contrib import messages
from articulos.models import Articulos, Categoria
from articulos.forms import FromArticulo, FromCategoria

#Categorias
# URLConf->MVT
def lista_articulos(request):
    articulos = Articulos.objects.all()
    #select * from articulos_articulos;
    return render(request, 'articulos.html', {'articulos': articulos})

def eliminar_articulos(request, id):
    Articulos.objects.get(id=id).delete()
    messages.error(request, 'Se elimino un articulo.')
    return redirect('articulos_lista')

def nuevo_articulo(request):
    if request.method == 'POST':#viene por post
        form = FromArticulo(request.POST)
        if form.is_valid():
            form.save()
            messages.error(request, 'Se agrego un nuevo articulo.')
            return redirect('articulos_lista')
    else:#viene por get
        form = FromArticulo()
        return render(request, 'nuevo_articulo.html',  {'form':form})

def editar_articulos(request, id):
    articulo = Articulos.objects.get(id=id) 
    if request.method == 'POST':#viene por post
        form = FromArticulo(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            messages.error(request, 'Se modifico un articulo.')
            return redirect('articulos_lista')
    else:#viene por get
        form = FromArticulo(instance=articulo)
        return render(request, 'nuevo_articulo.html',  {'form':form})

#Categorias
def lista_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoriatemplates/categorias.html', {'categorias':categorias})

def nueva_categoria(request):
    if request.method == 'POST':#viene por post
        form = FromCategoria(request.POST)
        if form.is_valid():
            form.save()
            messages.error(request, 'Se agrego nueva categoria.')
            return redirect('categoria_lista')
    else:#viene por get
        form = FromCategoria()
        return render(request, 'categoriatemplates/nueva_categoria.html',  {'form':form})

def eliminar_categoria(request, id):
    #Categoria.objects.get(id=id).delete()
    #messages.error(request, 'Se elimino una categoria.')
    categoria_eliminar = Categoria.objects.get(id=id)
    if  Articulos.objects.filter(categoria=categoria_eliminar):
            messages.error(request, 'No se puede elimiar la categoria, tiene articulos asociados.')
    else:
        categoria_eliminar.delete()
        messages.error(request, 'Se elimino con exito la categoria.')
    return redirect('categoria_lista')

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id) 
    if request.method == 'POST':#viene por post
        form = FromCategoria(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.error(request, 'Se modifico una categoria.')
            return redirect('categoria_lista')
    else:#viene por get
        form = FromCategoria(instance=categoria)
        return render(request, 'categoriatemplates/editar_categoria.html',  {'form':form})
