from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELDS = 'email'
    REQUIRED_FIELDS = []

    
