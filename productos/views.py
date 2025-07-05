from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Categoria, Producto
from django.urls import reverse
from .forms import CategoriaForm, ProductoForm

# Create your views here.

# Vistas para Categorías
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'productos/categorias/lista.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada correctamente')
            return redirect('productos:lista_categorias')
    else:
        form = CategoriaForm()
    
    return render(request, 'productos/categorias/crear.html', {'form': form})

def detalle_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = categoria.productos.all()
    return render(request, 'productos/categorias/detalle.html', {
        'categoria': categoria,
        'productos': productos
    })

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada correctamente')
            return redirect('productos:detalle_categoria', categoria_id=categoria.id)
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'productos/categorias/editar.html', {'categoria': categoria, 'form': form})

def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada correctamente')
        return redirect('productos:lista_categorias')
    
    return render(request, 'productos/categorias/eliminar.html', {'categoria': categoria})

# Vistas para Productos
def lista_productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    categoria_id = request.GET.get('categoria')
    
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    
    return render(request, 'productos/productos/lista.html', {
        'productos': productos,
        'categorias': categorias,
        'categoria_seleccionada': int(categoria_id) if categoria_id else None
    })

def crear_producto(request):
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Producto creado correctamente')
                return redirect('productos:lista_productos')
            except Exception as e:
                messages.error(request, f'Error al crear el producto: {str(e)}')
    else:
        form = ProductoForm()
    
    return render(request, 'productos/productos/crear.html', {'categorias': categorias, 'form': form})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'productos/productos/detalle.html', {'producto': producto})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Producto actualizado correctamente')
                return redirect('productos:detalle_producto', producto_id=producto.id)
            except Exception as e:
                messages.error(request, f'Error al actualizar el producto: {str(e)}')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'productos/productos/editar.html', {
        'producto': producto,
        'categorias': categorias,
        'form': form
    })

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente')
        return redirect('productos:lista_productos')
    
    return render(request, 'productos/productos/eliminar.html', {'producto': producto})
