from django.db import models
from django.contrib.auth.models import User
from rater.ratings import RATING_CHOICES

# Create your models here.
class Name(models.Model):
    user = models.ForeignKey(User, on_delete='CASCADE')
    name = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    starred = models.BooleanField(default=False)
    is_rated = models.BooleanField(default=False)
    rated_at = models.DateTimeField()
