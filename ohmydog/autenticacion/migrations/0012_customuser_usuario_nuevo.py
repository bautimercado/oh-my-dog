# Generated by Django 4.2 on 2023-06-05 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0011_remove_customuser_nuevousuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='usuario_nuevo',
            field=models.BooleanField(default=True),
        ),
    ]
