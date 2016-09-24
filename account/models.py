from django.db import models

# Create your models here.

class usersN(models.Model):
    username = models.CharField(max_length=16)
    nickname = models.CharField(max_length=16)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=32)
    type = models.CharField(max_length=8)
    rating = models.DecimalField(max_digits=1, decimal_places=1)
