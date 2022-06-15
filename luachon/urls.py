from django.urls import path
from . import views

app_name = "luachon"
urlpatterns = [
    path('', views.index, name = 'index'),
    path('detail/<int:question_id>', views.detail, name = "detail"),
    path('list/', views.xemds_question, name = 'list'),
    path('<int:question_id>', views.vote, name= "vote"),
]