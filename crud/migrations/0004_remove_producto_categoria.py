# Generated by Django 5.0.6 on 2024-06-21 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_alter_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
    ]
