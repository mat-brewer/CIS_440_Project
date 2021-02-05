from django.db import models
from main import models as main
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(main.MenuItem)

    def __str__(self):
        return  f'Order #{self.id}'