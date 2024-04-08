from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Manufacturer,Product
# Create your views here.

def Home(request):
    return render(request,template_name='base.html')

class ProductDetailView(DetailView):
    model=Product
    template_name = 'product/products_detail.html'


class ProductList(ListView):

    model= Product
    template_name = 'product/product_list.html'
