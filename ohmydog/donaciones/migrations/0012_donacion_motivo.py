# Generated by Django 4.2.1 on 2023-06-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donaciones', '0011_alter_donacion_monto'),
    ]

    operations = [
        migrations.AddField(
            model_name='donacion',
            name='motivo',
            field=models.TextField(default='', max_length=200),
        ),
    ]