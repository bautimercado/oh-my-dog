# Generated by Django 4.2.1 on 2023-06-08 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0004_perro_sexo_alter_perro_raza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='sexo',
            field=models.CharField(choices=[('macho', 'Macho'), ('hembra', 'Hembra')], default='', max_length=10, null=True),
        ),
    ]
