from django import forms
from django.db.models import fields
from .models import login

class login_form(forms.ModelForm):
    class Meta:
        model = login
        fields = ['username', 'password', 'email']