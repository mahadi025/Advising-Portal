from course import views
from django.urls import path

urlpatterns = [
    path("offered-courses/", views.offered_courses, name="offered-courses"),
    path(
        "instructor-class-schedule/",
        views.instructor_class_schedule,
        name="instructor-class-schedule",
    ),
    path(
        "instructor-section/<str:pk>/",
        views.instructor_section,
        name="instructor-section",
    ),
    path(
        "edit-grade/<str:pk>/",
        views.edit_grade,
        name="edit-grade",
    ),
    path(
        "student-class-schedule/",
        views.student_class_schedule,
        name="student-class-schedule",
    ),
    path(
        "student-grade-report/",
        views.student_grade_report,
        name="student-grade-report",
    ),
]
