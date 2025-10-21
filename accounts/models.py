from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(blank=True, null=True, verbose_name='avatar')
    birth_date = models.DateField(blank=True, null=True,verbose_name="birth date")

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'