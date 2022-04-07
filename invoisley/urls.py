from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gateway/', include("gateway.urls")),
    path('blogs/', include("blog.urls")),
    
]
