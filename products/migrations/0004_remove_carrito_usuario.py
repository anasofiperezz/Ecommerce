# Generated by Django 4.2 on 2023-05-15 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_productos_carrito_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='usuario',
        ),
    ]
