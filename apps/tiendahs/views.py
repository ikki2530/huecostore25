from django.shortcuts import render
from .models import Producto, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    queryset = request.GET.get("buscar") #buscar es el name del formulario, la clave en el diccionario
    productos = Producto.objects.filter(estado = True)
    print(queryset)
    if queryset:
        productos = Producto.objects.filter(
            Q(nombreProducto__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    paginator = Paginator(productos, 4) #instancia de la clase Paginator
    page = request.GET.get('page') # página en la que nos encontramos
    productos = paginator.get_page(page)

    print(request.GET)

    print(productos)
    return render(request, 'index.html', {'productos': productos})


def detalleProducto(request, slug):

    producto = get_object_or_404(Producto, slug = slug)
    
    return render(request, 'mostrarProducto.html', {'detalle_producto':producto })


def hogar(request):
    queryset = request.GET.get("buscar")
    productos = Producto.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Hogar')
    )

    if queryset:
        productos = Producto.objects.filter(
            Q(nombreProducto__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Hogar'),

        ).distinct()

    paginator = Paginator(productos, 4) #instancia de la clase Paginator
    page = request.GET.get('page') # página en la que nos encontramos
    productos = paginator.get_page(page)

    return render(request, 'hogar.html', {'productos':productos})


def modaAccesorios(request):
    queryset = request.GET.get("buscar")
    productos = Producto.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Moda & Accesorios')
    )

    if queryset:
        productos = Producto.objects.filter(
            Q(nombreProducto__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Moda & Accesorios')
        ).distinct()

    paginator = Paginator(productos, 4) #instancia de la clase Paginator
    page = request.GET.get('page') # página en la que nos encontramos
    productos = paginator.get_page(page)

    return render(request, 'modaAccesorios.html', {'productos':productos})
