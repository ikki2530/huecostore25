# Generated by Django 2.2.7 on 2019-11-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Categoría')),
                ('estado', models.BooleanField(default=True, verbose_name='categía Activada/Categoría no Activada')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombresProveedor', models.CharField(max_length=100, verbose_name='Nombres Proveedor')),
                ('apellidosProveedor', models.CharField(max_length=100, verbose_name='Apellidos Proveedor')),
                ('celular', models.CharField(max_length=15, verbose_name='Celular')),
                ('nombreEmpresa', models.CharField(max_length=50, verbose_name='Nombre Empresa')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('estado', models.BooleanField(default=True, verbose_name='Proveedor Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]
