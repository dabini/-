from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.IntegerField(default=10)
    gender = models.CharField(default="Male",  max_length=128)