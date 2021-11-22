from django.db import models
from mirage import fields
class Department(models.Model):
    dept_name = models.CharField(max_length=5,null=True,blank=True)
    building=models.CharField(max_length=20,null=True, blank=True)
    def __str__(self):
        return self.dept_name

class ClassRoom(models.Model):
    building=models.CharField(max_length=20,null=True, blank=True)
    room_number=models.CharField(max_length=7,null=True, blank=True)
    capacity=models.IntegerField(2,null=True,blank=True)


class Course(models.Model):
    course_id=models.CharField(max_length=7,null=True, blank=True)
    title=models.CharField(max_length=50,null=True, blank=True)
    credits=models.FloatField(max_length=2,null=True,blank=True)
    department=models.ForeignKey(Department, null=True, blank=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.course_id
    
class Section(models.Model):
    semester_choice={
        ('Spring','Spring'),
        ('Fall','Fall'),
        ('Summer','Summer')
    }
    courseId=models.ForeignKey(Course, null=True,blank=True,on_delete=models.SET_NULL)
    sec_id=models.IntegerField(null=True, blank=True)
    semester=models.CharField(max_length=6,null=True,blank=True,choices=semester_choice)
    year=models.IntegerField(null=True, blank=True)
    building=models.CharField(max_length=20,null=True,blank=True)
    roomNumber=models.ForeignKey(ClassRoom, null=True, blank=True,on_delete=models.SET_NULL)
 
class Student(models.Model):
    blood_group_list = {
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B+", "B-"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
    }
    department_list = {
        ("CSE", "CSE"),
        ("EEE", "EEE"),
        ("BBA", "BBA"),
        ("ICE", "ICE"),
        ("ENG", "ENG"),
    }
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    # img= models.ImageField(upload_to='pics',null=True,blank=True,default=0)
    password1 = fields.EncryptedCharField()
    password2 = fields.EncryptedCharField()
    student_id = models.CharField(max_length=13, unique=True, null=False)
    # admitted_semester=models.CharField(max_length=30,null=True,blank=True)
    # advisor=models.CharField(max_length=30,null=True,blank=True)
    # blood_group=models.CharField(max_length=3,null=True,blank=True,choices=blood_group_list)
    # present_address=models.CharField(max_length=50,null=True,blank=True)
    # phone_number=models.CharField(max_length=14,null=True,blank=True)
    department=models.ForeignKey(Department, null=True, blank=True,on_delete=models.SET_NULL)
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    def __str__(self):
        return self.student_id 
    
class Takes(models.Model):
    grade_list={
        ('A+','A+'),
        ('A','A'),
        ('A-','A-'),
        ('B+','B+'),
        ('B','B'),
        ('B-','B-'),
        ('C+','C+'),
        ('C','C'),
        ('C-','C-'),
        ('D+','D+'),
        ('D','D'),
        ('F','F')
    }
    course=models.ForeignKey(Course, null=True, blank=True,on_delete=models.SET_NULL)
    student=models.ForeignKey(Student, null=True, blank=True,on_delete=models.SET_NULL)
    grade=models.CharField(max_length=2,null=True,blank=True,choices=grade_list)
    def __str__(self):
        student_name=self.student.first_name+" "+self.student.last_name
        return student_name
    
class Prereq(models.Model):
    course=models.ForeignKey(Course, null=True, blank=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.prereq_id