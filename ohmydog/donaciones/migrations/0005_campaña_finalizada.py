# Generated by Django 4.2 on 2023-06-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donaciones', '0004_alter_donacion_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaña',
            name='finalizada',
            field=models.BooleanField(default=False),
        ),
    ]
