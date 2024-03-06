from django.shortcuts import render, redirect
from account.forms import CreateUserForm, EditStudentProfile, EditInstructorProfile
from core.models import Instructor, Student, Advisor
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or Password is incorrect")

    return render(request, "account/login.html")


def student_register(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            student_id = user.username
            user.save()
            group = Group.objects.get(name="student")
            user.groups.add(group)
            Student.objects.create(
                user=user,
                student_id=student_id,
                first_name=user.first_name,
                last_name=user.last_name,
            )
            login(request, user)
            return redirect("home")
    context = {"form": form}
    return render(request, "account/student_registration.html", context)


def instructor_register(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            instructor_id = user.username
            user.save()
            group = Group.objects.get(name="instructor")
            user.groups.add(group)
            Instructor.objects.create(
                user=user,
                instructor_id=instructor_id,
                first_name=user.first_name,
                last_name=user.last_name,
            )
            login(request, user)
            return redirect("home")
    context = {"form": form}
    return render(request, "account/instructor_registration.html", context)


def logout_user(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def profile(request):
    group = request.user.groups.all()[0].name
    if group == "instructor":
        user = request.user.instructor
        context = {"user": user}
    else:
        advisor = Advisor.objects.filter(
            student__student_id=request.user.username
        ).first()
        user = request.user.student
        context = {"advisor": advisor, "user": user}
    return render(request, "account/profile.html", context)


@login_required(login_url="login")
def edit_profile(request):
    group = request.user.groups.all()[0].name
    if group == "instructor":
        instructor = request.user.instructor
        user = instructor
        form = EditInstructorProfile(instance=instructor)
        if request.method == "POST":
            form = EditInstructorProfile(
                request.POST, request.FILES, instance=instructor
            )
            if form.is_valid():
                form.save()
                return redirect("profile")
    else:
        student = request.user.student
        user = student
        form = EditStudentProfile(instance=student)
        if request.method == "POST":
            form = EditStudentProfile(request.POST, request.FILES, instance=student)
            if form.is_valid():
                form.save()
                return redirect("profile")
    context = {"form": form, "user": user}
    return render(request, "account/edit_profile.html", context)
