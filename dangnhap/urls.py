from django.urls import path
from .views import logindemo

urlpatterns = [
    path('', logindemo.as_view(), name = 'login'),
]