from django.urls import path
from . import views

# app_name = "hold"
urlpatterns = [
    path('', views.index, name = 'blog'),
    path('<int:id>', views.PostDetail, name = 'detail'),
]