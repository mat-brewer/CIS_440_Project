from django.db import models


# Create your models here.
class MenuItem(models.Model):
    item_Name = models.CharField(max_length=200, default="")
    item_Price = models.FloatField(default=0.00)
    item_Ingredients = models.CharField(max_length=200, default="")

    def __str__(self):
        return f'{self.item_Name} | ${self.item_Price}'