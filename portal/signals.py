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
        advisingStudent=instance.advisingStudent  
        print(instance.section.timeSlot.day[0])
        section=instance.section
        takes=Takes.objects.create(takes_id=advisingStudent.student,section=section)
        print(f'Credits Taken {advisingStudent.creditsTaken}')
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
    instance.advisingStudent.save()