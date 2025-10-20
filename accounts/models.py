from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    class SocialMediaChoice(models.Choices):
        instagram = 'Instagaram'
        linkedin = 'LinkedIn'
        facebook = 'Facebook'
        x = 'X'

    email = models.EmailField(verbose_name='email')
    avatar = models.ImageField(blank=True, null=True, verbose_name='avatar')
    age = models.IntegerField(default=0, verbose_name='age')
    socialmedia = models.CharField(max_length=100, choices=SocialMediaChoice, default=SocialMediaChoice.instagram, verbose_name='socialmedia')

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'