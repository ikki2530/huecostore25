# Generated by Django 2.2.7 on 2019-11-27 18:59

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiendahs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(max_length=100, verbose_name='Nombre Producto')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
                ('contenido', ckeditor.fields.RichTextField()),
                ('precioProveedor', models.IntegerField(verbose_name='Precio del Proveedor')),
                ('precioPromocion', models.IntegerField(verbose_name='Precio Promoción')),
                ('precioVenta', models.IntegerField(verbose_name='Precio de Venta')),
                ('imagen', models.ImageField(upload_to='productos/')),
                ('estado', models.BooleanField(default=True, verbose_name='Publicado/No Publicado')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendahs.Categoria')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendahs.Proveedor')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
