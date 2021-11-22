from django.urls import path
from .import views
from django.conf.urls import url
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cgpa/', views.cgpa, name='cgpa'),
    path('profile/',views.profile, name='profile'),
    path('studentRegister/',views.studentRegister,name='studentRegister'),
    path('Offered_courses/',views.offered_courses, name='Offered_courses'),
]
