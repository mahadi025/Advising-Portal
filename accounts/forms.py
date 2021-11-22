from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentFrom(ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Student
        # fields = [
        #     "student_id",
        #     "password1",
        #     "password2",
        #     "email",
        #     "first_name",
        #     "last_name",
        # ]
        fields='__all__'