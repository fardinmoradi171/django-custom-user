from django.contrib import admin
from .models import Blog,BlogLike,BlogComment,BlogDislike
admin.site.register((Blog,BlogLike,BlogDislike,BlogComment))

# Register your models here.
