# Generated by Django 4.0.2 on 2022-03-06 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0006_autor_fecha_creacion_libro_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='estado'),
        ),
    ]
