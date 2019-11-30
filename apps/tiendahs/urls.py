from django.urls import path
from .views import *

urlpatterns = [
    path('', home , name='index'),
    path('hogar/', hogar, name = 'hogar'),
    path('modaAccesorios/', modaAccesorios, name = 'modaAccesorios'),
    path('<slug:slug>/', detalleProducto, name = 'detalle_producto'),
]
