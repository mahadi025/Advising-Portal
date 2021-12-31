from django.shortcuts import render, redirect,HttpResponse
from .models import *
from .forms import *
from accounts.models import *
from django.contrib import messages

def advising(request):
    # offeredSections=Section.objects.filter(year=2019,semester='Summer').order_by('id')
    offeredSections=Section.objects.all().order_by('id')
    if AdvisingStudent.objects.filter(student=request.user.student):
        advisingStudent=AdvisingStudent.objects.get(student=request.user.student)
    else:
        advisingStudent=AdvisingStudent.objects.create(student=request.user.student)
    advisedSections=AdvisingSlip.objects.filter(advisingStudent=advisingStudent)
    contex={'offeredSections':offeredSections,'advisedSections':advisedSections}
    return render(request,'advising.html',contex)

def add_course(request,pk):
    if AdvisingStudent.objects.filter(student=request.user.student):
        advisingStudent=AdvisingStudent.objects.get(student=request.user.student)
    else:
        advisingStudent=AdvisingStudent.objects.create(student=request.user.student)
    section=Section.objects.get(id=pk)
    semester=section.semester
    year=section.year
    course=section.course.course_id
    advisingStudent.creditsTaken+=section.course.credits
    student=Student.objects.get(studentId=request.user.username)
    if section.capacity>0:
        if Prereq.objects.filter(course=section.course):
            prereq=Prereq.objects.get(course=section.course)
            prereqCourse=prereq.prereqCourse
            if prereqCourse in student.completedCourses:
                print(prereqCourse+' course completed for '+course)   
                if advisingStudent.creditsTaken<=13.5:
                    if not AdvisingSlip.objects.filter(advisingStudent=advisingStudent):
                        AdvisingSlip.objects.create(advisingStudent=advisingStudent,section=section,semester=semester,year=year,course=course)
                    else:
                        if not AdvisingSlip.objects.filter(advisingStudent=advisingStudent,course=course):
                            AdvisingSlip.objects.create(advisingStudent=advisingStudent,section=section)
                            messages.success(request, 'Successfully added ' + course)
                        else:
                            messages.error(request,course+' already taken')
                else:
                    messages.error(request,'Maximum 13.5 credits can be taken')
            else:
                print(prereqCourse+' course  not completed for '+course)
                messages.error(request,prereqCourse+' not completed')
        else:
            if advisingStudent.creditsTaken<=13.5:
                if not AdvisingSlip.objects.filter(advisingStudent=advisingStudent,course=course):
                    AdvisingSlip.objects.create(advisingStudent=advisingStudent,section=section,semester=semester,year=year,course=course)
                    messages.success(request, 'Successfully added ' + course)
                else:
                    messages.error(request,course+' already taken prereq')
            else:
                messages.error(request,'Maximum 13.5 credits can be taken')
    else:
        messages.error(request,'No seat available for '+course+' '+section.secId)
    return redirect('advising')


def slipPrint(request):
    advisingStudent=AdvisingStudent.objects.get(student=request.user.student)
    advisedSections=AdvisingSlip.objects.filter(advisingStudent=advisingStudent)
    contex={'advisedSections':advisedSections}
    return render(request,'slip.html',contex)

def delete_course(request,pk):
    advisingSlip=AdvisingSlip.objects.get(id=pk)
    advisingSlip.delete()
    return redirect('advising')