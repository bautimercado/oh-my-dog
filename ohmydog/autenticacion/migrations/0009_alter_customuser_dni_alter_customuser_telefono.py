# Generated by Django 4.2 on 2023-06-04 22:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0008_alter_customuser_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='dni',
            field=models.CharField(error_messages={'unique': 'Ya existe un usuario con este DNI'}, max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telefono',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^[0-9+-]+$', 'El teléfono solo puede contener números y los caracteres "+" y "-".')]),
        ),
    ]
