from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    # possibly link the order that they had and show the food they ordered for this review.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=200, default="")
    would_you_reccommend_our_restaraunt = models.BooleanField(choices=BOOL_CHOICES)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'review_text')


    def __str__(self):
        return f'{self.user} Review #{self.id}'