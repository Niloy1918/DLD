import email
from django.db import models

# Create your models here.

class Accounts(models.Model):
    email = models.EmailField(max_length=254, default='user1@mailinator.com') 
    username = models.CharField(max_length=1000,blank=True)
    password = models.CharField(max_length=1000,blank=True)
    password2 = models.CharField(max_length=1000,blank=True)

    class Meta:
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.email