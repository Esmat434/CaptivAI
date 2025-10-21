from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    class SocialMediaChoice(models.TextChoices):
        INSTAGRAM = 'Instagram', 'Instagram'
        LINKEDIN = 'LinkedIn', 'LinkedIn'
        FACEBOOK = 'Facebook', 'Facebook'
        X = 'X', 'X'

    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(blank=True, null=True, verbose_name='avatar')
    socialmedia = models.CharField(
        max_length=100, 
        choices=SocialMediaChoice, 
        default=SocialMediaChoice.INSTAGRAM, 
        verbose_name='socialmedia'
    )
    birth_date = models.DateField(verbose_name="birth date")

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'