from django.shortcuts import render, redirect,HttpResponse
from .models import *
from .forms import *
from accounts.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def advising(request):
    year=2021
    semester='Spring'
    offeredSections=Section.objects.filter(year=year,semester=semester).order_by('id')
    if AdvisingStudent.objects.filter(student=request.user.student):
        advisingStudent=AdvisingStudent.objects.get(student=request.user.student)
    else:
        advisingStudent=AdvisingStudent.objects.create(student=request.user.student)
    advisedSections=AdvisingSlip.objects.filter(advisingStudent=advisingStudent,section__semester=semester)
    contex={'offeredSections':offeredSections,'advisedSections':advisedSections,'year':year,'semester':semester}
    return render(request,'advising.html',contex)

@login_required(login_url='login')
def add_course(request,pk):
    if AdvisingStudent.objects.filter(student=request.user.student):
        advisingStudent=AdvisingStudent.objects.get(student=request.user.student)
    else:
        advisingStudent=AdvisingStudent.objects.create(student=request.user.student)
    section=Section.objects.get(id=pk)
    semester=section.semester
    year=section.year
    course=section.course.course_id
    timeSlot=section.timeSlot
    advisingStudent.creditsTaken+=section.course.credits
    if section.course.title!='LAB':
        day1=section.timeSlot.day[0]
        day2=section.timeSlot.day[1]
        if day1=='S' and day2=='T':
            advisingStudent.sundayClass+=1
            advisingStudent.tuesdayClass+=1
        elif day1=='M' and day2=='W':
            advisingStudent.mondayClass+=1
            advisingStudent.wednesdayClass+=1
        elif day1=='T' and day2=='R':
            advisingStudent.tuesdayClass+=1
            advisingStudent.thursdayClass+=1
        elif day1=='S' and day2=='R':
            advisingStudent.sundayClass+=1
            advisingStudent.thursdayClass+=1
    student=Student.objects.get(studentId=request.user.username)
    if section.capacity>0:
        if Prereq.objects.filter(course=section.course):
            prereq=Prereq.objects.get(course=section.course)
            prereqCourse=prereq.prereqCourse
            if prereqCourse in student.completedCourses:
                print(prereqCourse+' course completed for '+course)   
                if advisingStudent.creditsTaken<=13.5:
                    if advisingStudent.sundayClass <= 2 and advisingStudent.mondayClass <= 2 and advisingStudent.tuesdayClass <=2 and advisingStudent.wednesdayClass and advisingStudent.thursdayClass <= 2:
                        print('Section can be added') 
                        if not AdvisingSlip.objects.filter(advisingStudent=advisingStudent):
                            AdvisingSlip.objects.create(advisingStudent=advisingStudent,section=section,semester=semester,year=year,course=course,timeSlot=timeSlot)
                        else:
                            if not AdvisingSlip.objects.filter(advisingStudent=advisingStudent,course=course):
                                if not AdvisingSlip.objects.filter(advisingStudent=advisingStudent,timeSlot=timeSlot):
                                    AdvisingSlip.objects.create(advisingStudent=advisingStudent,section=section)
                                    messages.success(request, 'Successfully added ' + course)
                                else:
                                    messages.error(request,'Timeslot conflicted')
                            else:
                                messages.error(request,course+' already taken')
                    else:
                        messages.error(request,'You can not take more than 2 classes per day')
                else:
                    messages.error(request,'Maximum 13.5 credits can be taken')
            else:
                print(prereqCourse+' course  not completed for '+course)
                messages.error(request,prereqCourse+' not completed')
        else:
            if advisingStudent.creditsTaken<=13.5:
                if advisingStudent.sundayClass <= 2 and advisingStudent.mondayClass <= 2 and advisingStudent.tuesdayClass <=2 and advisingStudent.wednesdayClass and advisingStudent.thursdayClass <= 2:
                    if not AdvisingSlip.objects.filter(advisingStudent=advisingStudent):
                        AdvisingSlip.objects.create(advisingStudent=advisingStudent,section=section,semester=semester,year=year,course=course,timeSlot=timeSlot)
                    else:
                        if not AdvisingSlip.objects.filter(advisingStudent=advisingStudent,course=course):
                            if not AdvisingSlip.objects.filter(advisingStudent=advisingStudent,timeSlot=timeSlot):
                                AdvisingSlip.objects.create(advisingStudent=advisingStudent,section=section)
                                messages.success(request, 'Successfully added ' + course)
                            else:
                                messages.error(request,'Timeslot conflicted')
                        else:
                            messages.error(request,course+' already taken')
                else:
                    messages.error(request,'You can not take more than 2 classes per day')
            else:
                messages.error(request,'Maximum 13.5 credits can be taken')
    else:
        messages.error(request,'No seat available for '+course+' '+section.secId)
    return redirect('advising')

@login_required(login_url='login')
def slipPrint(request):
    advisingStudent=AdvisingStudent.objects.get(student=request.user.student)
    advisedSections=AdvisingSlip.objects.filter(advisingStudent=advisingStudent)
    contex={'advisedSections':advisedSections,'advisingStudent':advisingStudent}
    return render(request,'slip.html',contex)
@login_required(login_url='login')
def delete_course(request,pk):
    advisingSlip=AdvisingSlip.objects.get(id=pk)
    advisingSlip.delete()
    return redirect('advising')