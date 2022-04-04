from django.db import models
from user.models import CustomUser
# Create your models here.

class Jwt(models.Model):
    user = models.OneToOneField(CustomUser,related_name="user_name", on_delete=models.CASCADE)
    access = models.TextField()
    refresh = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.email
