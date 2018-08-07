from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    is_rated = models.BooleanField(default=False)
    rated_at = models.DateTimeField()
