from django.urls import path
from .views import GSI, LoginView,RegisterView, RefreshView


# path of repo = https://github.com/fardinmoradi171/django-custom-user.git

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('refresh', RefreshView.as_view(), name='refreshtoken'),
    path('secure-info', GSI.as_view(), name='secureinfo')
]
