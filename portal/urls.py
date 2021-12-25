from django.urls import path
from .import views

urlpatterns=[
    path('advising/',views.advising,name='advisingSlip'),
]