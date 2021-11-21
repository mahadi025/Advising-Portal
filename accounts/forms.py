from django.forms import ModelForm
from .models import Student
from django import forms


class StudentFrom(ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Student
        fields = "__all__"
