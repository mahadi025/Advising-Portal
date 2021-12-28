from django.urls import path
from .import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.studentRegisterPage, name='register'),
    path('InstructorRegister/', views.instructorRegisterPage, name='instructorRegisterPage'),
    
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('cgpa/', views.cgpa, name='cgpa'),
    
    path('profile/',views.profile, name='profile'),
    
    path('TakesSection/',views.takes,name='takesSection'),
    
    path('schedule/',views.schedule, name='schedule'),
    
    path('Offered_courses/',views.offered_courses, name='Offered_courses'),
    path('grade_report/',views.student_grade_report, name='grade_report'),
    
    path('EditStudentProfile/',views.editStudentProfile,name='editStudentProfile'),
    path('EditInstructorProfile/',views.editInstructorProfile,name='editInstructorProfile'),
    
    path('Section/',views.section, name='section'),
    
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_complete'),
    
]
