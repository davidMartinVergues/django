# Generated by Django 4.0.2 on 2022-03-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0004_alter_libro_autor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autor_id',
        ),
        migrations.AddField(
            model_name='libro',
            name='autor_id',
            field=models.ManyToManyField(to='libro.Autor'),
        ),
    ]
