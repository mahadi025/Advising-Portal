from django.db.models.signals import post_save
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
            print('Student created')
            print(kwargs)
            print(f'Sender: {sender}')
            print(created)
            print(instance)
            instance.save()
        else:
            Instructor.objects.create(user=instance, instructorId=instance.username,firstName=instance.first_name,lastName=instance.last_name,email=instance.email)
            
@receiver(post_save,sender=Takes)
def add_course(sender, instance,created,**kwargs):
    if created:
        if not instance.grade=='F':
            student=Student.objects.get(studentId=instance.takes_id.studentId)
            course=instance.section.course.course_id
            print("Course: "+course)
            if Prereq.objects.filter(course=course):
                prereq=Prereq.objects.get(course=course)
                prereqCourse=prereq.prereqCourse
                print("Prereq Course: "+prereqCourse)
                if prereqCourse in student.completedCourses:
                    print(prereqCourse+" completed")
                    if not instance.section.course.course_id in student.completedCourses:
                        student.completedCourses.append(instance.section.course.course_id)
                        if student.tot_cred==0.0:
                            student.tot_cred=instance.section.course.credits
                        else:
                            student.tot_cred+=instance.section.course.credits
                        instance.section.capacity-=1
                        instance.section.save()
                        student.save()
                        instance.save()
                else:
                    instance.delete()
                    print(prereqCourse+" not completed")
            else:
                if not instance.section.course.course_id in student.completedCourses:
                        student.completedCourses.append(instance.section.course.course_id)
                        if student.tot_cred==0.0:
                            student.tot_cred=instance.section.course.credits
                        else:
                            student.tot_cred+=instance.section.course.credits
                        instance.section.capacity-=1
                        instance.section.save()
                        student.save()
                        instance.save()
        if instance.section.course.credits>3.0:
            title=instance.section.course.title
            labCourse=Course.objects.get(course_id=str(instance.section.course.course_id)+'L',title='LAB',credits=0.0)
            section=Section.objects.get(course=labCourse,secId=instance.section.secId,year=instance.section.year,semester=instance.section.semester,
                                        instructor=instance.section.instructor)
            Takes.objects.create(takes_id=instance.takes_id,section=section)
            section.save()
            instance.save()