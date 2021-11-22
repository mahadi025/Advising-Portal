# from django.db import models

# # from accounts .models import Student

# class ClassRoom(models.Model):
#     building=models.CharField(max_length=20,null=True, blank=True)
#     room_number=models.CharField(max_length=7,null=True, blank=True)
#     capacity=models.IntegerField(2,null=True,blank=True)


# class Course(models.Model):
#     course_id=models.CharField(max_length=7,null=True, blank=True)
#     title=models.CharField(max_length=50,null=True, blank=True)
#     credits=models.FloatField(max_length=2,null=True,blank=True)
#     department=models.ForeignKey(Department, null=True, blank=True,on_delete=models.SET_NULL)
#     def __str__(self):
#         return self.course_id
    
# class Section(models.Model):
#     semester_choice={
#         ('Spring','Spring'),
#         ('Fall','Fall'),
#         ('Summer','Summer')
#     }
#     courseId=models.ForeignKey(Course, null=True,blank=True,on_delete=models.SET_NULL)
#     sec_id=models.IntegerField(null=True, blank=True)
#     semester=models.CharField(max_length=6,null=True,blank=True,choices=semester_choice)
#     year=models.IntegerField(null=True, blank=True)
#     building=models.CharField(max_length=20,null=True,blank=True)
#     roomNumber=models.ForeignKey(ClassRoom, null=True, blank=True,on_delete=models.SET_NULL)
    
# class Takes(models.Model):
#     grade_list={
#         ('A+','A+'),
#         ('A','A'),
#         ('A-','A-'),
#         ('B+','B+'),
#         ('B','B'),
#         ('B-','B-'),
#         ('C+','C+'),
#         ('C','C'),
#         ('C-','C-'),
#         ('D+','D+'),
#         ('D','D'),
#         ('F','F')
#     }
#     course=models.ForeignKey(Course, null=True, blank=True,on_delete=models.SET_NULL)
#     student=models.ForeignKey(Student, null=True, blank=True,on_delete=models.SET_NULL)
#     grade=models.CharField(max_length=2,null=True,blank=True,choices=grade_list)
#     def __str__(self):
#         student_name=self.student.first_name+" "+self.student.last_name
#         return student_name
    
# class Prereq(models.Model):
#     course=models.ForeignKey(Course, null=True, blank=True,on_delete=models.SET_NULL)
#     def __str__(self):
#         return self.prereq_id