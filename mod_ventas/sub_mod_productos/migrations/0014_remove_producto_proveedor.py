# Generated by Django 5.0.2 on 2024-07-29 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_mod_productos', '0013_rename_proveedor_id_producto_proveedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='proveedor',
        ),
    ]
