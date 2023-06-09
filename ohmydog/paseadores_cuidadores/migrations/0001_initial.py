# Generated by Django 4.1.7 on 2023-05-07 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import paseadores_cuidadores.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaseadorCuidador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomyap', models.CharField(max_length=50)),
                ('dni', models.CharField(error_messages={'unique': 'Ya existe un usuario con este DNI'}, max_length=30, unique=True)),
                ('textolibre', models.TextField(max_length=200))
            ],
        ),
    ]
