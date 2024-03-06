from advising import views
from django.urls import path

urlpatterns = [
    path("advising/", views.advising, name="advising"),
    path("add-course/<str:pk>/", views.add_course, name="add-course"),
    path("delete-course/<str:pk>/", views.delete_course, name="delete-course"),
    path("advisor-advising/", views.advisor_advising, name="advisor-advising"),
    path("print-slip/", views.print_slip, name="print-slip"),
]
