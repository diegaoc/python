# Generated by Django 5.0.3 on 2024-04-03 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ListaReproduccion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contrasena',
            new_name='password',
        ),
    ]
