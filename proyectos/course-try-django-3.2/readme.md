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

## Recumerando objetos 

```python

article_obj = Article.objects.get(id=2)
articles_all = Article.objects.all()
```
