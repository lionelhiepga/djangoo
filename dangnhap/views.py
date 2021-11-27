from django import views
from django.shortcuts import render
from django.views.generic.base import View
from .forms import login_form
from django.http import HttpResponse
from django.views import View


# Create your views here.
class logindemo(View):
    
    def get(self,request):
        f = login_form
        return render(request, 'dangnhap/dangnhap.html', {'f': f})
    
    def post(self,request):
        f = login_form(request.POST)
        if not f.is_valid():
            return HttpResponse("ban nhap sai du lieu roi")
        else:
            f.save()
            return render(request, 'dangnhap/ketqua.html')