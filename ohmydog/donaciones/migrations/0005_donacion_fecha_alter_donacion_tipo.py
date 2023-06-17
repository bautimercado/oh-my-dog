# Generated by Django 4.2.1 on 2023-06-17 19:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('donaciones', '0004_alter_donacion_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='donacion',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='donacion',
            name='tipo',
            field=models.CharField(max_length=12),
        ),
    ]
