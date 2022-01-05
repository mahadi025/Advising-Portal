from django.urls import path
from .import views

urlpatterns=[
    path('advising/',views.advising,name='advising'),
    path('course/<str:pk>/',views.add_course,name='course'),
    path('facultyAddCourse/<str:pk>/',views.faculty_add_course,name='facultyAddCourse'),
    path('facultyDeleteCourse/<str:pk>/',views.faculty_delete_course,name='facultyDeleteCourse'),
    path('advisorCourse/<str:pk>/',views.advisor_add_course,name='advisorAddCourse'),
    path('deleteCourse/<str:pk>/',views.delete_course,name='deleteCourse'),
    path('advisorDeleteCourse/<str:pk>/',views.advisor_delete_course,name='advisorDeleteCourse'),
    path('slip/',views.slipPrint,name='slip',),
    path('facultyAdvising/',views.facultyAdvising,name='facultyAdvising'),
    path('advisorAdvising/',views.advisorAdvising,name='advisorAdvising'),
]