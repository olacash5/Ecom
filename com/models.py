from django.db import models

# Create your models here.


class Seller(models.Model):
    Business_name = models.CharField(max_length=50)
    Product = models.CharField(max_length=100)
