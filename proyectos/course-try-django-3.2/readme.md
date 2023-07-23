# Django course from CodingEntrepreneurs - youTube

source https://youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL


# ORM de django

## Creando objetos en django

Desde la consola de django

```
python manage.py shell
```

Podemos probar las distintas maneras de crear objetos en django:

De manera automática Django crea un campo ID (primary key) para todos los modelos.
Cuando creamos los objeto debemos especificar los atributos como keyarguments

```

from apps.articles.models import Article

# 1 manera

obj1 = Article(title='title3',content='content3')
obj1.save()

# 2 manera

 Article.objects.create(title='title4',content='content4')

# de este modo NO necesitas hacer save() 


```

## Recuperando objetos 

```python

article_obj = Article.objects.get(id=2)
# <Article: Article object (4)>
articles_all = Article.objects.all()
# <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
```

* Cuando usamos get solo puede devolver un registro y el tipo de objeto que devuelve es el del modelo

* cuando usamos all() nos devuelve un querySet es decir un array de objetos del tipo del modelo


