from django.db import models
from user.models import CustomUser

# Create your models here.

class Blog(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    description = models.TextField(editable=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class BlogComment(models.Model):
    blog = models.ForeignKey(Blog,related_query_name="CB",on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    text = models.CharField(max_length=555)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.email
    
class BlogLike(models.Model):
    blog = models.ForeignKey(Blog,related_query_name="CL",on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.blog.title
    
class BlogDislike(models.Model):
    blog = models.ForeignKey(Blog,  on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.blog.title