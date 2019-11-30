from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la Categoría', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('categía Activada/Categoría no Activada', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now= False, auto_now_add = True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural= 'Categorías'

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    id = models.AutoField(primary_key = True)
    nombresProveedor = models.CharField('Nombres Proveedor', max_length = 100, null = False, blank = False)
    apellidosProveedor = models.CharField('Apellidos Proveedor', max_length = 100, null = False, blank = False)
    celular = models.CharField('Celular', max_length = 15, null = False, blank = False)
    nombreEmpresa = models.CharField('Nombre Empresa', max_length = 50, null = False, blank = False)
    direccion = models.CharField('Dirección', max_length = 100, null = False, blank = False)
    correo = models.EmailField('Correo Electrónico', blank = False, null = False)
    estado = models.BooleanField('Proveedor Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return "{0} {1}".format(self.nombresProveedor, self.apellidosProveedor)


class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombreProducto = models.CharField('Nombre Producto', max_length = 100, null = False, blank = False)
    slug = models.CharField('Slug', max_length = 100, null = False, blank = False)
    descripcion = models.CharField('Descripción', max_length = 100, blank = False)
    contenido = RichTextField()
    precioProveedor = models.IntegerField('Precio del Proveedor', null = False, blank = False)
    precioAntes = models.IntegerField('Precio Antes', null = False, blank = False, default = 0)
    precioVenta = models.IntegerField('Precio de Venta',  null = False, blank = False, default = 0)
    medioPago = models.CharField('Medio de pago', max_length = 120, blank = False, default = 'Contra entrega')
    tiempoEntrega = models.CharField('Tiempo de entrega', max_length = 120, blank = False, default = '2 días máximo')
    imagen = models.ImageField(upload_to = 'productos/', null = False, blank = False)
    imagen2 = models.ImageField(upload_to = 'productos/', null = True, blank = True)
    imagen3 = models.ImageField(upload_to = 'productos/', null = True, blank = True)
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default = True)
    descuento = models.BooleanField('Descuento/No Descuento', default = True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombreProducto
