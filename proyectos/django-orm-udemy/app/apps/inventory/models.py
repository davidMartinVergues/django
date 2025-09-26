from django.db import models

class Category(models.Model):
     name = models.CharField(max_length=50,null=True)
     is_active = models.BooleanField(default=True)
     level = models.SmallIntegerField(null=True)
     
     class Meta:
          db_table='category'
class PromotionEvent(models.Model):
     pass
class Product(models.Model):
     description = models.TextField(null=True)
     price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
     slug = models.SlugField(max_length=50)
class ProductPromotionEvent(models.Model):
     pass
class StockManagement(models.Model):
     pass
class User(models.Model):
     pass
class Order(models.Model):
     pass
class OrderProduct(models.Model):
     pass
