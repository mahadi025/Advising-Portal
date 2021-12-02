from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import Group, auth
from django.contrib import messages
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,EditStudentProfile,EditInstructorProfile
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users

@unauthenticated_user
def studentRegisterPage(request):    
    form=CreateUserForm()    
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data['username']
            group=Group.objects.get(name='student')
            user.groups.add(group)
            Student.objects.create(user=user, studentId=username,firstName=user.first_name,lastName=user.last_name,email=user.email)
            return redirect('login')

    contex={'form':form}
    return render(request,'register.html',contex)

def instructorRegisterPage(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data['username']
            group=Group.objects.get(name='instructor')
            user.groups.add(group)
            Instructor.objects.create(user=user, instructorId=username,firstName=user.first_name,lastName=user.last_name,email=user.email)
            return redirect('login')
    contex={'form':form}
    return render(request,'InstructorRegister.html',contex)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username=request.POST['studentId']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')    
    contex={}
    return render(request,'login.html',contex)


def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def profile(request):
    group=request.user.groups.all()[0].name
    if group=='instructor':
        return render(request,"InstructorProfile.html")
    else:
        return render(request, "StudentProfile.html")

def instructorprofile(request):
    return render(request,'InstructorProfile.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['student','admin'])
def cgpa(request):
    return render(request, "cgpa calculator.html")


@login_required(login_url='login')
def offered_courses(request):
    if request.method == "POST":
        semester = request.POST["semester"]
        year = request.POST["year"]
        sections = Section.objects.filter(semester=semester,year=year).order_by('course')
        contex={'sections':sections,'semester':semester,'year':year}
        return render(request, "Offered_courses.html", contex)
    else:
        return render(request, "Offered_courses.html")
    
@allowed_users(allowed_roles=['student'])
def student_grade_report(request):
    if request.method =='POST':
        semester=request.POST["semester"]
        year=request.POST["year"]
        print(semester)
        print(year)
        student_id=request.user.student.studentId
        takes=Takes.objects.filter(takes_id=student_id,section__semester=semester,section__year=year).order_by('section__course')
        contex={'takes':takes}
        return render(request, "GradeReport.html",contex)
    return render(request,'GradeReport.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def editStudentProfile(request):
    student=request.user.student
    form=EditStudentProfile(instance=student)
    if request.method =='POST':
        form=EditStudentProfile(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect('profile')
    contex={'form':form}
    return render(request,'EditStudentProfile.html',contex)

@login_required(login_url='login')
@allowed_users(allowed_roles=['instructor'])
def editInstructorProfile(request):
    instructor=request.user.instructor
    form=EditInstructorProfile(instance=instructor)
    if request.method =='POST':
        form=EditInstructorProfile(request.POST,request.FILES,instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('profile')
    contex={'form':form}
    return render(request,'EditInstructorProfile.html',contex)


def section(request):
    if request.method == 'POST':
        semester = request.POST["semester"]
        year = request.POST["year"]
        sections=Section.objects.filter(instructor=request.user.instructor.instructorId,semester=semester,year=year)
        contex={'sections':sections}
        return render(request,'Section.html',contex)
    return render(request,'Section.html')
        
