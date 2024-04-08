from django.contrib import admin
from django.urls import path,include

from  .views import ProductList,ProductDetailView, Home
from . import apps

apps_name = apps.ProductConfig.name

urlpatterns = [
    path('',Home, name='home'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(),name='product-detail')
]
