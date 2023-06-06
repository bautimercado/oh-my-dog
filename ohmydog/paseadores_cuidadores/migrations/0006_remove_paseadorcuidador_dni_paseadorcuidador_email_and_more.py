# Generated by Django 4.2.1 on 2023-06-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paseadores_cuidadores', '0005_alter_paseadorcuidador_dni'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paseadorcuidador',
            name='dni',
        ),
        migrations.AddField(
            model_name='paseadorcuidador',
            name='email',
            field=models.EmailField(default='', error_messages={'unique': 'Ya existe un paseador o cuidador con este email'}, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='paseadorcuidador',
            name='tipo',
            field=models.CharField(choices=[('Paseador', 'Paseador'), ('Cuidador', 'Cuidador')], default='Paseador', max_length=10),
        ),
    ]