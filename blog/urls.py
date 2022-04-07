from django.urls import path
from .views import BlogList,BlogDetail,CreateBlog,Create

urlpatterns = [
    path('', BlogList),
    path('<int:id>', BlogDetail),
    path('create', CreateBlog),
    path('crt', Create),
    
]