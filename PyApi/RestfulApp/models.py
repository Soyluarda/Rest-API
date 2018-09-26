from django.db import models

# Create your models here.
class Motors(models.Model):
    name = models.CharField(max_length=150)
    speed = models.IntegerField()
