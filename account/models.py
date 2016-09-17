from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=16)
    nickname = models.CharField(max_length=16)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=32)
    style = models.UUIDField(primary_key=False)
    rating = models.DecimalField(max_digits=1, decimal_places=1)
