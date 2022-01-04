from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createAdvisingSlip(ModelForm):
    class Meta:
        model=AdvisingSlip
        fields=['section','advisingStudent']