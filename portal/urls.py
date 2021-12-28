from django.urls import path
from .import views

urlpatterns=[
    path('advising/',views.advising,name='advising'),
    path('advisingSlip/',views.create_advisingSlip,name='advisingSlip'),
    path('course/<str:pk>/',views.add_course,name='course'),
]