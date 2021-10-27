from django.db import models


# Create your models here.
class Specifications(models.Model):
    subcategories = (('Laptop', 'Laptop'), ('Mobile', 'Mobile'), ('Tennis', 'Tennis'), ('Cricket', 'Cricket'))
    categories = (('Electronics', 'Electronics'), ('Sports', 'Sports'))
    Products = models.CharField(max_length=20)
    SubCategories = models.CharField(max_length=20, choices=subcategories)
    Categories = models.CharField(max_length=20, choices=categories)
