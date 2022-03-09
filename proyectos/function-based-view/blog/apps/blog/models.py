from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Categoria(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre de la categoria', max_length=100, null=False, blank=False)
    estado = models.BooleanField('categoria activada/desactivada', default=True)
    fecha_creacion = models.DateField('fecha de creacion', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nombre  


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField("Nombres del Autor", max_length=255, null=False, blank=False)
    apellidos = models.CharField("Apellidos del Autor", max_length=255, null=False, blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Web', null=True, blank=True)
    email = models.EmailField("Correo electronico", null=False, blank=False)
    estado = models.BooleanField("Autor activo/desactivado", default=True)
    fecha_creacion = models.DateField("Fecha de creacion", auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural= 'Autores'

    def __str__(self):
        return f'{self.apellidos} {self.nombres}'


class Post (models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=90, null=False, blank=False)
    slug = models.CharField("Slug", max_length=100,null=False, blank=False)
    description = models.CharField("Descripcion", max_length=100,null=False, blank=False)
    imagen = models.URLField(max_length=255,null=False, blank=False) # renderizar imagenes desde internet, si tuvieramos un server con almacenamiento de archivos sería un campo ImageField
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField("Publicado/no publicado", default=True)
    fecha_creacion = models.DateField("fecha de creacion", auto_now=False, auto_now_add=True)
    contenido = RichTextField("Contenido")

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__ (self):
        return self.titulo

    