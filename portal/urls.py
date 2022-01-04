from django.urls import path
from .import views

urlpatterns=[
    path('advising/',views.advising,name='advising'),
    path('course/<str:pk>/',views.add_course,name='course'),
    path('facultyCourse/<str:pk>/',views.faculty_add_course,name='facultyAddCourse'),
    path('deleteCourse/<str:pk>/',views.delete_course,name='deleteCourse'),
    path('facultyDeleteCourse/<str:pk>/',views.faculty_delete_course,name='facultyDeleteCourse'),
    path('slip/',views.slipPrint,name='slip',),
    path('facultyAdvising/',views.facultyAdvising,name='facultyAdvising')
]