# Generated by Django 4.2.1 on 2023-07-10 21:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paseadores_cuidadores', '0013_valoracion_average_valoracion_content_type_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='valoracion',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='valoracion',
            name='puntaje',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.RemoveField(
            model_name='valoracion',
            name='average',
        ),
        migrations.RemoveField(
            model_name='valoracion',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='valoracion',
            name='count',
        ),
        migrations.RemoveField(
            model_name='valoracion',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='valoracion',
            name='total',
        ),
    ]
