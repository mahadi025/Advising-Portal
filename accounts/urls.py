from django.urls import path
from .import views
from django.conf.urls import url
urlpatterns = [
    path('register/', views.studentRegisterPage, name='register'),
    path('InstructorRegister/', views.instructorRegisterPage, name='instructorRegisterPage'),
    
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('cgpa/', views.cgpa, name='cgpa'),
    
    path('profile/',views.profile, name='profile'),
    
    path('Offered_courses/',views.offered_courses, name='Offered_courses'),
    path('grade_report/',views.student_grade_report, name='grade_report'),
    
    path('EditStudentProfile/',views.editStudentProfile,name='editStudentProfile'),
    path('EditInstructorProfile/',views.editInstructorProfile,name='editInstructorProfile'),
    
    path('Section/',views.section, name='section'),
    
]
