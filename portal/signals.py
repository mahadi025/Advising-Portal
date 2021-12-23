from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.dispatch import receiver

from accounts.models import Student
from .models import AdvisingStudent

# @receiver(post_save,sender=advisingStudent)
# def create_advisingStudent(sender,instance,created,**kwargs):
#     student = Student.objects.get(instance)
#     if created:
#         # advisingStudent.objects.create(user=instance,studentId=instance.username,firstName=student.first_name,lastName=instance.last_name,email=instance.email) 
#         print ("Advising Student created")
#         instance.save()