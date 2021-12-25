from django.db.models.signals import post_save
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
            takes=Takes.objects.create(takes_id=advisingStudent.student,section=instance.section)
            advisingStudent.creditsTaken+=instance.section.course.credits
            instance.save()
            takes.save()
        else:
            instance.delete()
            print ('Maximum credits taken')
            