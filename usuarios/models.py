from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    avatar = models.ImageField(upload_to='avatares/', blank=True, null=True)
    username = models.CharField(max_length=150, unique=True,)
