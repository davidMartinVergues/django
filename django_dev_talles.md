# CUrso Django - devtalles


## HOF - Higher order function 


funcion es que reciben otras funciones como argumento y devuelve funciones

## estructura del proyecto 

### asgi.py (Asynchronous Server Gateway Interface)

Permite ejecutar Django en servidores asíncronos (p. ej. Uvicorn, Daphne, Hypercorn) y soportar WebSockets, HTTP/2, long-polling y tareas async.
Si necesitas WebSockets (canales en tiempo real), mezclar vistas async y sync, o sencillamente quieres un stack moderno.

```python
from django.core.asgi import get_asgi_application
application = get_asgi_application()
```
Ejemplo de despliegue:
`uvicorn myproject.asgi:application --host 0.0.0.0 --port 8000`

### wsgi.py (Web Server Gateway Interface)

El estándar “clásico” sincrónico de Python.
Ejecutar Django en servidores WSGI como Gunicorn/uWSGI detrás de Nginx/Apache para HTTP tradicional.
Si tu app es puramente sincrónica (sin WebSockets) y tu hosting/infra está pensada para WSGI.

```python
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
 
```
Ejemplo de despliegue:
`gunicorn myproject.wsgi:application -b 0.0.0.0:8000`