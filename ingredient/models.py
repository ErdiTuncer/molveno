from django.db import models

# Create your models here.


class Ingredient(models.Model):
    """..."""
    name = models.CharField(max_length=64)
    price = models.FloatField()
    stock_required = models.IntegerField()
    stock_total = models.IntegerField()
    type = models.CharField(max_length=64)

    def __str__(self):
        return self.name