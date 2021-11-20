from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import User
from django.conf import settings

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        studentId = request.POST['studentId']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # img=request.POST['img']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(studentId=studentId).exists():
                messages.info(request, 'Student Id already exists')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(
                    request, 'This email is already register with an account')
                return redirect('register')
            else:
                user = User.objects.create_user(password=password1,email=email,studentId=studentId,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request, 'User Created')
                return redirect('home')
        else:
            messages.info(request, 'Password did not match')
            return redirect('register')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        studentId=request.POST['studentId']
        password = request.POST['password']
        user=auth.authenticate(password=password,studentId=studentId)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def profile(request):
    return render(request, 'Student_profile.html')

def cgpa(request):
    return render(request,"cgpa calculator.html")