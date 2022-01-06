from django.shortcuts import render, redirect,HttpResponse
from django.forms import inlineformset_factory
from accounts.views import section
from .models import *
from .forms import *
from accounts.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user,allowed_users
from django.http import HttpResponseRedirect


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
@allowed_users(allowed_roles=['student'])
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
@allowed_users(allowed_roles=['student'])
def slipPrint(request):
    advisingStudent=AdvisingStudent.objects.get(student=request.user.student)
    advisedSections=AdvisingSlip.objects.filter(advisingStudent=advisingStudent)
    contex={'advisedSections':advisedSections,'advisingStudent':advisingStudent}
    return render(request,'slip.html',contex)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def delete_course(request,pk):
    advisingSlip=AdvisingSlip.objects.get(id=pk)
    advisingSlip.delete()
    return redirect('advising')

def set_studentId(studentId):
    global AdvisingStudentId
    AdvisingStudentId=studentId
    
@login_required(login_url='login')
@allowed_users(allowed_roles=['instructor'])
def facultyAdvising(request):
    year=2021
    semester='Spring'
    instructorId=request.user.username
    instructor=Instructor.objects.get(instructorId=instructorId)
    offeredSections=Section.objects.filter(year=year,semester=semester,instructor=instructor).order_by('id') 
    if request.method == 'POST':
        studentId=request.POST["studentId"]
        if Student.objects.filter(studentId=studentId):
            student=Student.objects.get(studentId=studentId)
            set_studentId(studentId)
            advisingStudent=AdvisingStudent.objects.get(student=student)
            advisedSections=AdvisingSlip.objects.filter(advisingStudent=advisingStudent,section__semester=semester,section__year=year)
            contex={'offeredSections':offeredSections,'year':year,'semester':semester,'advisedSections':advisedSections}
            return render(request,'FacultyAdvising.html',contex)
        else:
            messages.error(request,'No student found')
    return render(request,'SelectStudent.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['instructor'])
def faculty_add_course(request,pk):
    studentId=AdvisingStudentId
    student=Student.objects.get(studentId=studentId)
    if AdvisingStudent.objects.filter(student=student):
        advisingStudent=AdvisingStudent.objects.get(student=student)
    else:
        advisingStudent=AdvisingStudent.objects.create(student=student)
    section=Section.objects.get(id=pk)
    semester=section.semester
    year=section.year
    course=section.course.course_id
    timeSlot=section.timeSlot
    advisingStudent.creditsTaken+=section.course.credits
    instructor=Instructor.objects.filter(instructorId=request.user.username)
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
    student=Student.objects.get(studentId=studentId)
    if section.capacity>0:
        if Prereq.objects.filter(course=section.course):
            prereq=Prereq.objects.get(course=section.course)
            prereqCourse=prereq.prereqCourse
            if prereqCourse in student.completedCourses:
                print(prereqCourse+' course completed for '+course)   
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
                    messages.error(request,'Student can not take more than 2 classes per day')
            else:
                messages.error(request,prereqCourse+' not completed')
        else:
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
                messages.error(request,'Student can not take more than 2 classes per day')
    else:
        messages.error(request,'No seat available for '+course+' '+section.secId)
    section=Section.objects.get(id=pk)
    student=Student.objects.get(studentId=AdvisingStudentId)
    advisingStudent=AdvisingStudent.objects.filter(student=student)
    advisedSections=AdvisingSlip.objects.filter(advisingStudent_id=advisingStudent)
    # advisingStudent=AdvisingStudent.objects.get(advisingslip=advisingSlip)
    # print(advisingSlip)
    print(AdvisingStudentId)
    # print(advisingSlip)
    offeredSections=Section.objects.filter(year=year,semester=semester,instructor=request.user.instructor).order_by('id')
    # advisedSections=AdvisingSlip.objects.filter(advisingStudent=advisingStudent)
    contex={'offeredSections':offeredSections,'year':year,'semester':semester,'advisedSections':advisedSections}
    return render(request,'FacultyAdvising.html',contex)
    # return redirect('facultyAdvising')


@login_required(login_url='login')
@allowed_users(allowed_roles=['instructor'])
def faculty_delete_course(request,pk):
    advisingSlip=AdvisingSlip.objects.get(id=pk)
    advisingStudent=AdvisingStudent.objects.get(advisingslip=advisingSlip)
    advisingSlip.delete()
    semester='Spring'
    year=2021
    offeredSections=Section.objects.filter(year=year,semester=semester,instructor=request.user.instructor).order_by('id')
    advisedSections=AdvisingSlip.objects.filter(advisingStudent=advisingStudent)
    contex={'offeredSections':offeredSections,'year':year,'semester':semester,'advisedSections':advisedSections}
    # return redirect('facultyAdvising')
    return render(request,'FacultyAdvising.html',contex)


@login_required(login_url='login')
@allowed_users(allowed_roles=['instructor'])
def advisorAdvising(request):
    year=2021
    semester='Spring'
    instructor=request.user.instructor
    offeredSections=Section.objects.filter(year=year,semester=semester).order_by('id')
    if request.method == 'POST':
        studentId=request.POST["studentId"]
        if Student.objects.filter(studentId=studentId):
            student=Student.objects.get(studentId=studentId)
            set_studentId(studentId)
            if Advisor.objects.filter(instructor=instructor,student=student):
                advisingStudent=AdvisingStudent.objects.get(student=student)
                advisedSections=AdvisingSlip.objects.filter(advisingStudent=advisingStudent,section__semester=semester,section__year=year)
                contex={'offeredSections':offeredSections,'year':year,'semester':semester,'advisedSections':advisedSections}
                return render(request,'AdvisorAdvising.html',contex)
            else:
                messages.error(request,'You are not his/her Advisor')
        else:
            messages.error(request,'No student found')
    return render(request,'SelectStudent.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['instructor'])
def advisor_add_course(request,pk):
    studentId=AdvisingStudentId
    student=Student.objects.get(studentId=studentId)
    if AdvisingStudent.objects.filter(student=student):
        advisingStudent=AdvisingStudent.objects.get(student=student)
    else:
        advisingStudent=AdvisingStudent.objects.create(student=student)
    section=Section.objects.get(id=pk)
    semester=section.semester
    year=section.year
    course=section.course.course_id
    timeSlot=section.timeSlot
    advisingStudent.creditsTaken+=section.course.credits
    instructor=Instructor.objects.filter(instructorId=request.user.username)
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
    student=Student.objects.get(studentId=studentId)
    if section.capacity>0:
        if Prereq.objects.filter(course=section.course):
            prereq=Prereq.objects.get(course=section.course)
            prereqCourse=prereq.prereqCourse
            if prereqCourse in student.completedCourses:
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
                    messages.error(request,'Student can not take more than 2 classes per day')
            else:
                messages.error(request,prereqCourse+' not completed')
        else:
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
                messages.error(request,'Student can not take more than 2 classes per day')
    else:
        messages.error(request,'No seat available for '+course+' '+section.secId)
    advisingStudent=AdvisingStudent.objects.get(student=student)
    advisedSections=AdvisingSlip.objects.filter(advisingStudent=advisingStudent,section__semester=semester)
    offeredSections=Section.objects.filter(year=year,semester=semester).order_by('id') 
    contex={'offeredSections':offeredSections,'year':year,'semester':semester,'advisedSections':advisedSections}
    # return render(request,'AdvisorAdvising.html',contex)
    return redirect('advisorAdvising')


@login_required(login_url='login')
@allowed_users(allowed_roles=['instructor'])
def advisor_delete_course(request,pk):
    year=2021
    semester='Spring'
    advisedSections=AdvisingSlip.objects.filter(id=pk)
    advisingSlip=AdvisingSlip.objects.get(id=pk)
    advisingSlip.delete()
    offeredSections=Section.objects.filter(year=year,semester=semester).order_by('id')
    contex={'offeredSections':offeredSections,'advisedSections':advisedSections,'year':year,'semester':semester}
    # return render(request,'AdvisorAdvising.html',contex)
    return redirect('advisorAdvising')