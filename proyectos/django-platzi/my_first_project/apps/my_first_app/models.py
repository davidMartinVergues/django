from django.db import models

# Create your models here.

class Car(models.Model):
    
    title = models.TextField(max_length=255)