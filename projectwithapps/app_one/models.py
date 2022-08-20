from django.db import models


# Create your models here.
class Product(models.Model):
    Product_id = models.IntegerField()
    Product_name = models.CharField(max_length=25)
    prices = models.FloatField()
    discount = models.IntegerField()
    description = models.TextField()

    def _str_(self):
        return self.Product

