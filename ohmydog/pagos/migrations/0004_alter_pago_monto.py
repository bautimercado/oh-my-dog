# Generated by Django 4.1.7 on 2023-05-31 00:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0003_delete_tarjeta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0, 'El monto a pagar debe ser mayor o igual a 0')]),
        ),
    ]
