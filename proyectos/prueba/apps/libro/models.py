from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apeliidos = models.CharField(max_length=220, blank=False, null=False)
    nacionaldad = models.CharField(max_length=200, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)