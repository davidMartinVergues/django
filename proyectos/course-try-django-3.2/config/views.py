"""
To render html web pages
"""


from  django.http import HttpResponse
from apps.articles.models import Article




# function views
def home_view(request):

    article_obj = Article.objects.get(id=2)
    articles_all = Article.objects.all()

    print(type(article_obj))
    print(type(articles_all))
    print(article_obj.title)
    print(articles_all[0].title)

    """
    Take in a request (Django sends request)
    Return HTML as a response 
    """

    name = 'David'

    HTML_STRING = f"""
    <h1>Hello {name}!!</h1>
    """
    return HttpResponse(HTML_STRING)