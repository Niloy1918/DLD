from email.policy import default
from enum import unique
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class MyUserManager(BaseUserManager):
    def createUser(self, email, device_id, password=None):
        if not email:
            raise ValueError("email is required")
        if not device_id:
            raise ValueError("device_id is required")
        

class MyUser(AbstractBaseUser):
    email= models.EmailField(verbose_name = "email", max_length = 70, unique=True)
    device_id= models.CharField(verbose_name = "device_id", null=True, blank=True)
    date_joined= models.DateTimeField(verbose_name = "date_joined", auto_now_add=True)
    is_admin= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)

    USERNAME_FIELD="email"

    REQUIRED_FIELDS=['email','device_id']

    def __str__(self):
        return self.device_id

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

