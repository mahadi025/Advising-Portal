from django.db.models.signals import post_save,post_delete
from django.shortcuts import render, redirect
from django.dispatch import receiver
from accounts.models import *
from .models import *
from django.contrib import messages

@receiver(post_save,sender=AdvisingSlip)
def create_advisingSlip(sender, instance,created,**kwargs):
    if created:
        instance.semester=instance.section.semester
        instance.year=instance.section.year
        instance.course=instance.section.course.course_id
        instance.timeSlot=instance.section.timeSlot
        advisingStudent=instance.advisingStudent  
        section=instance.section
        takes=Takes.objects.create(takes_id=advisingStudent.student,section=section)
        if section.course.credits>3.0:
            labCourse=Course.objects.get(course_id=str(instance.section.course.course_id)+'L',title='LAB',credits=0.0)
            labSection=Section.objects.get(course=labCourse,secId=instance.section.secId,year=instance.section.year,semester=instance.section.semester,
                                        instructor=instance.section.instructor)
            labSlip=AdvisingSlip.objects.create(advisingStudent=instance.advisingStudent,section=labSection)
            section.capacity-=1
            labSection.capacity-=1
            labSection.save()
            labSlip.save()
            section.save()
        elif section.course.credits!=0.0: 
            section.capacity-=1
            section.save()
            takes.save()
        instance.advisingStudent.save()
        instance.save()
            
@receiver(post_delete,sender=AdvisingSlip)
def delete_advisingSlip(sender,instance,**kwargs):
    if Takes.objects.filter(section=instance.section,takes_id=instance.advisingStudent.student):
        takes=Takes.objects.get(section=instance.section,takes_id=instance.advisingStudent.student)
        takes.delete()
    instance.advisingStudent.creditsTaken-=instance.section.course.credits
    if instance.advisingStudent.creditsTaken<0:
        instance.advisingStudent.creditsTaken=0
    if instance.section.course.credits>3.0:
        labCourse=Course.objects.get(course_id=str(instance.section.course.course_id)+'L',title='LAB',credits=0.0)
        labsection=Section.objects.get(course=labCourse,secId=instance.section.secId,year=instance.section.year,semester=instance.section.semester,
                                        instructor=instance.section.instructor)
        lab=Takes.objects.filter(section=labsection)
        labSlip=AdvisingSlip.objects.filter(section=labsection)
        labsection.capacity+=1
        instance.section.capacity+=1
        labsection.save()
        lab.delete()
        labSlip.delete()
    elif instance.section.course.credits !=0.0:
        instance.section.capacity+=1
    instance.section.save()
    if instance.section.course.title !='LAB':
        day1=instance.section.timeSlot.day[0]
        day2=instance.section.timeSlot.day[1]
        if day1=='S' and day2=='T':
            instance.advisingStudent.sundayClass-=1
            instance.advisingStudent.tuesdayClass-=1
            if instance.advisingStudent.sundayClass < 0 and instance.advisingStudent.tuesdayClass < 0:
                instance.advisingStudent.sundayClass=0
                instance.advisingStudent.tuesdayClass=0
        elif day1=='M' and day2=='W':
            instance.advisingStudent.mondayClass-=1
            instance.advisingStudent.wednesdayClass-=1
            if instance.advisingStudent.mondayClass < 0 and instance.advisingStudent.wednesdayClass < 0:
                instance.advisingStudent.mondayClass=0
                instance.advisingStudent.wednesdayClass=0
        elif day1=='T' and day2=='R':
            instance.advisingStudent.tuesdayClass-=1
            instance.advisingStudent.thursdayClass-=1
            if instance.advisingStudent.tuesdayClass < 0 and instance.advisingStudent.thursdayClass < 0:
                instance.advisingStudent.tuesdayClass=0
                instance.advisingStudent.thursdayClass=0
        elif day1=='S' and day2=='R':
            instance.advisingStudent.sundayClass-=1
            instance.advisingStudent.thursdayClass-=1
            if instance.advisingStudent.sundayClass < 0 and instance.advisingStudent.thursdayClass < 0:
                instance.advisingStudent.sundayClass=0
                instance.advisingStudent.thursdayClass=0
    instance.advisingStudent.save()