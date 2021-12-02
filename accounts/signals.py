from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Student,Instructor
from django.contrib.auth.models import Group


def student_profile(sender,instance,created,**kwargs):
    if created:
        group=Group.objects.get(name='student')
        instance.groups.add(group)
        Student.objects.create(user=instance, studentId=instance.username,firstName=instance.first_name,lastName=instance.last_name)
post_save.connect(student_profile,sender=User)

def instructor_profile(sender,instance,created,**kwargs):
    if created:
        group=Group.objects.get(name='instructor')
        instance.groups.add(group)
        Instructor.objects.create(user=instance, instructorId=instance.username,firstName=instance.first_name,lastName=instance.last_name)
post_save.connect(instructor_profile,sender=User)