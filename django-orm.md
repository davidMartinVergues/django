# Django Database ORM Mastery

source: https://www.udemy.com/course/django-4x-orm-mastery/

## Starting new Django project


1. Crear un direcorio con el nombre de nuetsro proyecto y en ese directorio ejecutar el comando :

```
django-admin startproject projectName .

```
2. runserver

```python
python manage.py runserver
```

si queremos cambiar el puerto podemos especificarlo al final del comando 

```python
python manage.py runserver 8080

```
3. crear una app 

para ello podemos adoptar el enfoque de crear un directorio `apps` donde guardaremos todas las app q vayamos creando, para que este directorio funcione como un repo debemos crear en su interior un archivo `__ini__.py`.
Una vez hecho esto creamos las carpetas con el mismo nombre que tendrá nuestra app


creamos el árbol de directorio

```bash
mkdir -p apps/newapp
touch apps/__init__.py
```
creamos la app dentro 

```bash
python manage.py startapp newapp apps/newapp
```
Al crear la app dentro de un directorio debemos de modificar el archivo `apps.py` que se encuentra dentro de la nueva app 

![not found](img/54.png)

4. Una vez creada la nueva applicación debemos registrarla para que django conozca su existencia. 

![not found](img/53.png)

5. posteriormente tenemos que crear un superuser para poder entrar en el dashboard admin de django

```
python manage.py createsuperuser 
```

6. ejecutamos las migrackiones para generar en la bbdd (sqlite) las tablas por defecto de django

```
python manage.py migrate
```

## Django request-response cycle

![not found](img/55.png)

1. el user hace una request en el navegador, busca una url (127.0.0.1)
2. el servidor recoge esta petición y la lleva a django
3. en django busca si en el archivo de urls.py existe dicha url
4. si la encuentra la conecta con una view
5. las views son código que puede recoger datos de la bbdd(los modelos creados en el archivo `models.py`)y los pinta en una plantilla (html)
6. plantilla + datos es devuelto al browser del user


## URLs

en el directorio core de Django tenemos un archiv `url.py` donde guardamos las urls a las q responderá nuestra django app.

![not found](img/56.png)

1. si dejamos el nombre de la url vacío `path('', admin.site.urls),` hace referencia a nuetsra homepage
2. el patrón que utilizamos para definir la url nunca empieza por "/" pero siempre termina con el "/"

Lo que haremos ahora es conectar ese archivo urls.py del core con los archivos urls.py de las distintas apps q vayamos creando, en nuestro caso de la app `newapp`
y estas urls conectarlas con una view 
![not found](img/57.png)

por convención el name que le damos a la url es el mismo q el path

```python

urlpatterns = [
    path("home/", views.home, name='home')
]

```


