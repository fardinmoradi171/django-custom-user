from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager

# Create your models here.
class CustomUserMnamager(BaseUserManager):
    # Create user...
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("email is required..")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    # Create superuser.for check is_staff and is_superuser feature 
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('name',"admin")
        if extra_fields.get('is_staff') is not True:
            raise ValueError("superuser must have is_staff=true")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser must have is_superuser=true")
        return self._create_user(email,password,**extra_fields)
        


class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # change username field to email:
    USERNAME_FIELD = "email"
    objects =  CustomUserMnamager()
    
    def __str__(self):
        return self.email
