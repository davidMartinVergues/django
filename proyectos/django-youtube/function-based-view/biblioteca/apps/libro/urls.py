from django.urls import path
from .views import crearAutor, listarAutor, editarAutor, eliminarAutor, eliminarAutorV2, eliminarAutorV3

urlpatterns = [
    path('crear-autor/',crearAutor,name='crear_autor'),
    path('autores/',listarAutor,name='listar_autores'),
    path('editar-autor/<int:pk>', editarAutor, name='editar_autor'),
    path('eliminar-autor/<int:pk>', eliminarAutor, name= 'eliminar-autor'),
    path('eliminar-autorv2/<int:pk>',eliminarAutorV2, name='eliminar-autorv2' ),
    path('eliminar-autorv3/<int:pk>', eliminarAutorV3, name= 'eliminar-autorv3')
]
