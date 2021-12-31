from django.urls import path
from .import views

urlpatterns=[
    path('advising/',views.advising,name='advising'),
    path('course/<str:pk>/',views.add_course,name='course'),
    path('deleteCourse/<str:pk>/',views.delete_course,name='deleteCourse'),
    path('slip/',views.slipPrint,name='slip',)
]