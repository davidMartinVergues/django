# Generated by Django 4.0.2 on 2022-03-08 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='twitter'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='web',
            field=models.URLField(blank=True, null=True, verbose_name='Web'),
        ),
    ]
