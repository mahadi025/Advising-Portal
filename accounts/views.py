from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import *
from .forms import *
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users
from .termGPA import calculate

@unauthenticated_user
def studentRegisterPage(request):    
    form=CreateUserForm()    
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data['username']
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    contex={'form':form}
    return render(request,'register.html',contex)

def instructorRegisterPage(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='instructor')
            user.groups.add(group)
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
        advisor=Advisor.objects.filter(s__studentId=request.user.username).first()
        contex={'advisor':advisor}
        return render(request, "StudentProfile.html",contex)

def instructorprofile(request):
    return render(request,'InstructorProfile.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['student','instructor'])
def cgpa(request):
    return render(request, "cgpa calculator.html")


@login_required(login_url='login')
def offered_courses(request):
    if request.method == "POST":
        semester = request.POST["semester"]
        year = request.POST["year"]
        sections = Section.objects.filter(semester=semester,year=year).order_by('id')
        contex={'sections':sections,'semester':semester,'year':year}
        return render(request, "Offered_courses.html", contex)
    else:
        return render(request, "Offered_courses.html")
    
@allowed_users(allowed_roles=['student'])
def student_grade_report(request):
    if request.method =='POST':
        semester=request.POST["semester"]
        year=request.POST["year"]
        student_id=request.user.student.studentId
        takes=Takes.objects.filter(takes_id=student_id,section__semester=semester,section__year=year).order_by('section__course')

        termCGPA=calculate(username=student_id,year=year,semester=semester)
        contex={'takes':takes,'termCGPA':termCGPA}
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['instructor'])
def section(request):
    if request.method == 'POST':
        semester = request.POST["semester"]
        year = request.POST["year"]
        instructor=request.user.instructor
        sections=Section.objects.filter(instructor=instructor,semester=semester,year=year)
        contex={'sections':sections,'semester':semester,'year':year,'instructor':instructor}
        return render(request,'Section.html',contex)
    return render(request,'Section.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['instructor'])
def takes(request):
    if request.method =='POST':
        group=request.user.groups.all()[0].name
        if group=='instructor':
            semester = request.POST["semester"]
            year = request.POST["year"]
            user=request.user
            takes=Takes.objects.filter(section__instructor=user.username,section__year=year,section__semester=semester)
            contex={'takes':takes,'semester':semester,'year':year}
            return render(request, 'TakesSection.html',contex)
    return render(request,'TakesSection.html')
    
@login_required(login_url='login')
def schedule(request):
    if request.method == "POST":
        semester = request.POST["semester"]
        year = request.POST["year"]
        takes=Takes.objects.filter(takes_id=request.user.student,section__semester=semester,section__year=year).order_by('section__instructor__instructorId','section__course')
        contex={'takes':takes}
        print(semester)
        return render(request, "schedule.html", contex)
    else:
        return render(request, "schedule.html")