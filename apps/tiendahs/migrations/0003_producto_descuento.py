# Generated by Django 2.2.7 on 2019-11-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendahs', '0002_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descuento',
            field=models.BooleanField(default=True, verbose_name='Descuento/No Descuento'),
        ),
    ]
