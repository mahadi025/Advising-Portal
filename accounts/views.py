from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, auth
from django.contrib import messages
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users

@unauthenticated_user
def registerPage(request):    
    form=CreateUserForm()    
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            student_id=form.cleaned_data['username']
            group=Group.objects.get(name='student')
            user.groups.add(group)
            messages.success(request,'Account was created for '+student_id)
            return redirect('login')

    contex={'form':form}
    return render(request,'register.html',contex)

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
    return render(request, "Student_profile.html")

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def cgpa(request):
    return render(request, "cgpa calculator.html")

@login_required(login_url='login')
def offered_courses(request):
    # sections=Section.objects.filter(semester='Summer',year=2019)
    if request.method == "POST":
        semester = request.POST["semester"]
        year = request.POST["year"]
        # teaches = Teaches.objects.filter(section__semester=semester,section__year=year)
        # context = {"teaches": teaches,"semester":semester,"year":year}
        return render(request, "Offered_courses.html", )
    else:
        return render(request, "Offered_courses.html")