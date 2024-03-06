from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from core.models import Section, Takes, Student
from course.cgpa import calculate_gpa
from course.forms import EditGrade


def is_instructor(user):
    return user.groups.filter(name="instructor").exists()


def is_student(user):
    return user.groups.filter(name="student").exists()


@login_required(login_url="login")
def offered_courses(request):
    if request.method == "POST":
        semester = request.POST["semester"]
        year = request.POST["year"]
        sections = Section.objects.filter(semester=semester, year=year).order_by("id")
        context = {"sections": sections, "semester": semester, "year": year}
        return render(request, "course/offered_courses.html", context)
    else:
        return render(request, "course/offered_courses.html")


@login_required(login_url="login")
@user_passes_test(is_instructor, login_url="login")
def instructor_class_schedule(request):
    if request.method == "POST":
        semester = request.POST["semester"]
        year = request.POST["year"]
        instructor = request.user.instructor
        sections = Section.objects.filter(
            instructor=instructor, semester=semester, year=year
        )
        context = {
            "sections": sections,
            "semester": semester,
            "year": year,
            "instructor": instructor,
        }
        return render(request, "course/instructor_class_schedule.html", context)
    return render(request, "course/instructor_class_schedule.html")


@login_required(login_url="login")
@user_passes_test(is_instructor, login_url="login")
def instructor_section(request, pk):
    section = Section.objects.get(id=pk)
    takes = Takes.objects.filter(section=section)
    context = {"takes": takes, "section": section}
    return render(request, "course/instructor_section.html", context)


@login_required(login_url="login")
@user_passes_test(is_instructor, login_url="login")
def edit_grade(request, pk):
    take = Takes.objects.get(id=pk)
    student = Student.objects.get(student_id=take.takes_id.student_id)
    form = EditGrade(instance=take)
    context = {"form": form, "student": student}
    if request.method == "POST":
        form = EditGrade(request.POST, instance=take)
        if form.is_valid():
            form.save()
            return redirect("instructor-section", pk=take.section.id)
    return render(request, "course/edit_grade.html", context)


@login_required(login_url="login")
@user_passes_test(is_student, login_url="login")
def student_class_schedule(request):
    if request.method == "POST":
        semester = request.POST["semester"]
        year = request.POST["year"]
        takes = Takes.objects.filter(
            takes_id=request.user.student,
            section__semester=semester,
            section__year=year,
        ).order_by("section__instructor__instructor_id", "section__course")
        context = {"takes": takes, "semester": semester, "year": year}
        return render(request, "course/student_class_schedule.html", context)
    else:
        return render(request, "course/student_class_schedule.html")


@login_required(login_url="login")
@user_passes_test(is_student, login_url="login")
def student_grade_report(request):
    if request.method == "POST":
        semester = request.POST["semester"]
        year = request.POST["year"]
        student = request.user.student
        takes = Takes.objects.filter(
            takes_id=student, section__semester=semester, section__year=year
        ).order_by("section__course")

        term_CGPA = calculate_gpa(username=student, year=year, semester=semester)
        context = {
            "takes": takes,
            "term_CGPA": term_CGPA,
            "student": student,
            "semester": semester,
            "year": year,
        }
        return render(request, "course/student_grade_report.html", context)
    return render(request, "course/student_grade_report.html")
