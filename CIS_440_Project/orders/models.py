from django.db import models
from main import models as main
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(main.MenuItem)
    time_ordered = models.DateTimeField(auto_now_add=True)

    @property
    def order_total(self):
        list_of_items = []
        for item in self.items.all():
            list_of_items.append(item.item_Price)
        return f'Order Total: ${sum(list_of_items)}'

    def __str__(self):
        return  f'Order #{self.id} | Ordered at {self.time_ordered.time()}'

   