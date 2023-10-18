from django.contrib import admin

from .models import Autor, Categoria, Post
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoriaResource(resources.ModelResource):

    class Meta:
        model = Categoria

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # barra de búsqueda
    search_fields= ['nombre']
    list_display = ('id','nombre','estado','fecha_creacion')
    resource_class= CategoriaResource

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'email']
    list_display = ('nombres','apellidos','email', 'estado','fecha_creacion')
    resource_class = AutorResource
    



admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post)
