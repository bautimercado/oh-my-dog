# Generated by Django 4.2.1 on 2023-06-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0012_customuser_usuario_nuevo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='monto_a_favor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
