# Generated by Django 4.0.2 on 2022-03-08 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=255, verbose_name='Nombres del Autor')),
                ('apellidos', models.CharField(max_length=255, verbose_name='Apellidos del Autor')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('twitter', models.URLField(verbose_name='twitter')),
                ('instagram', models.URLField(verbose_name='Instagram')),
                ('web', models.URLField(verbose_name='Web')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electronico')),
                ('estado', models.BooleanField(default=True, verbose_name='Autor activo/desactivado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre de la categoria')),
                ('estado', models.BooleanField(default=True, verbose_name='categoria activada/desactivada')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
