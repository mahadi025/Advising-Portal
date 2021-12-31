from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        if '-' in instance.username: 
            group=Group.objects.get(name='student')
            instance.groups.add(group)
            Student.objects.create(user=instance, studentId=instance.username,firstName=instance.first_name,lastName=instance.last_name,email=instance.email)
            instance.save()
        else:
            Instructor.objects.create(user=instance, instructorId=instance.username,firstName=instance.first_name,lastName=instance.last_name,email=instance.email)
            
@receiver(post_save,sender=Takes)
def add_course(sender, instance,created,**kwargs):
    if created:
        if not instance.grade=='F':
            student=Student.objects.get(studentId=instance.takes_id.studentId)
            if not instance.section.course.course_id in student.completedCourses:
                    student.completedCourses.append(instance.section.course.course_id)
                    if student.tot_cred==0.0:
                        student.tot_cred=instance.section.course.credits
                    else:
                        student.tot_cred+=instance.section.course.credits
                    student.save()
                    instance.save()
            instance.section.save()
            
@receiver(post_delete,sender=Takes)
def delete_course(sender, instance,**kwargs):
    instance.takes_id.tot_cred-=instance.section.course.credits
    take=Takes.objects.filter(section=instance.section)
    take.delete()