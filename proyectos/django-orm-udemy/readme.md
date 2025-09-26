# Curso ORM - Udemy 

## Comandos

1. generar el schema de la bbdd con sus relaciones

si añadimos la `-s` solo genra el schema si quitamos las `-s` incluirá los inserts(datos)

```bash
pg_dump -h localhost -U postgres -d angular_django -n public -s > schema.sql
```

2. si queremos ver el sql de la migracion en concreto

```bash
docker compose run django python manage.py sqlmigrate inventory 0001

```
3.  lanzar comando en el contenedor

```bash
docker compose run django python manage.py migrate
```

## Configuracion de Modelo

Cuando creamos un modelo este se guardará en la bbdd con el nombre:

```
appname_modelNaMe

inventory_category
```

si queremos modificar este comportamiento debemos usar la `class Meta`

```python
class Product(models.Model):
     description = models.TextField(null=True)
     price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
     slug = models.SlugField(max_length=50) # ES CASE SENSITIVE
     class Meta:
        db_table = 'product'
```

Un campo `slug` sirve para poder crear una url friendly, por ejemplo usando el nombre del producto crear una url, para no tener q poner `products/134646` ponemos `products/red_shoe`

