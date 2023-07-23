- [Django](#django)



# Curso Django creación Backend REST API

source : [Build a Backend REST API with Python & Django - Advanced (Udemy)](https://www.udemy.com/course/django-python-advanced/)

## Tecnologías que utilizaremos en el curso

![not found](img/49.png)

También utilizaremos GitHub Actions con el objetivo de lanzar test automáticos cada vez que hagamos push al repo de github.

## Docker

Que beneficios nos trae docker para el desarrollo:

- Mayor consistencia entre el entorno de Desarrollo y producción ya que utilizaremos la misma imagen para ambos.
- Facilidad para colaborar ya que todos tienen las mismas dependencias
- Podemos especificar en archivos todas las dependencias tanto a nivel de SO como de nuestra app (Dockerfile)
- Permite dejar tu equipo local limpio

Para gestionar todas las dependencias y configurar el SSOO utilizaremos el Dockerfile

Con el objetivo de usar las github actions junto con dockerhub debemos configurar un par de cosas:

1. generar token en dockerhub para autenticarnos

![not found](img/50.png)

2. registrar en nuestro repo de github 2 secrets:
   1. nombre del user de dockerhub
   2. token para acceder a dockerhub

![not found](img/51png.png)

### Docker configuration

* Crear Dockerfile, donde especificaremos todas las dependencias a nivel de Sistema Operativo.
* Docker Compose, define cómo nuestra imagen de docker debe ser usada para ejecutar nuestro servidor de desarollo. Definiremos:
  * Cada imagen será un servicio y cada uno recibirá un nombre
  * puertos de acceso
  * volúmenes

```dockerfile

FROM python:3.9-alpine3.13
LABEL maintainer="David"

ENV PYTHONUNBUFFERED 1

```





