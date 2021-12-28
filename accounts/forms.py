from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'first_name', 'last_name','email','password1','password2']

class EditStudentProfile(ModelForm):
    class Meta:
        model = Student
        fields = ['img', 'phoneNumber', 'presentAddress','bloodGroup']

class EditInstructorProfile(ModelForm):
    class Meta:
        model = Instructor
        fields = ['img', 'phoneNumber', 'presentAddress','bloodGroup','dept_name']