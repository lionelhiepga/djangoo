from django import views
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, request
from .models import Postform


def index(request):
    pf = Postform.objects.all()
    return render(request, "blog/blog.html", {'pf': pf})

def PostDetail(request, id):
    pd = Postform.objects.get(id = id)
    return render(request, "blog/detail_blog.html", {'pd': pd})