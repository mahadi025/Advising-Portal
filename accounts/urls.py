from django.urls import path
from .import views
from django.conf.urls import url
urlpatterns = [
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^cgpa', views.cgpa, name='cgpa'),
    url(r'^profile',views.profile, name='profile'),
]
