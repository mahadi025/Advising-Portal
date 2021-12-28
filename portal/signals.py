from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.dispatch import receiver

from accounts.models import *
from .models import *

@receiver(post_save,sender=AdvisingSlip)
def create_advisingSlip(sender, instance,created,**kwargs):
    if created:
        advisingStudent=instance.advisingStudent
        if advisingStudent.creditsTaken<=13.5:
            print(instance.section.timeSlot.day[0])
            section=instance.section
            takes=Takes.objects.create(takes_id=advisingStudent.student,section=section)
            advisingStudent.creditsTaken+=instance.section.course.credits
            instance.save()
            takes.save()
            instance.advisingStudent.save()
        else:
            instance.delete()
            print ('Maximum credits taken')
            
@receiver(post_delete,sender=AdvisingSlip)
def delete_advisingSlip(sender,instance,**kwargs):
    # instance.section.capacity+=1
    # removedCourse=instance.advisingStudent.student.completedCourses
    # print(removedCourse)
    # for course in removedCourse:
    #     course.remove(instance.section.course.course_id)
    if Takes.objects.filter(section=instance.section):
        takes=Takes.objects.get(section=instance.section)
        takes.delete()
    instance.advisingStudent.creditsTaken-=instance.section.course.credits
    # instance.advisingStudent.student.tot_cred-=instance.section.course.credits
    if instance.advisingStudent.creditsTaken<0:
        instance.advisingStudent.creditsTaken=0
    # if instance.section.course.credits>3.0:
    #     labCourse=Course.objects.get(course_id=str(instance.section.course.course_id)+'L',title='LAB',credits=0.0)
    #     labsection=Section.objects.get(course=labCourse,secId=instance.section.secId,year=instance.section.year,semester=instance.section.semester,
    #                                     instructor=instance.section.instructor)
    #     lab=Takes.objects.get(section=labsection)
    #     labsection.capacity+=1
        # labsection.save()
        # lab.delete()
    # instance.section.save()
    instance.advisingStudent.save()
    # instance.advisingStudent.student.save()            