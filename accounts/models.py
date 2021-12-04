from django.db import models
from django.contrib.auth.models import User

class Classroom(models.Model):
    building = models.CharField(max_length=15)
    room_number = models.CharField(max_length=7)
    capacity = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        unique_together = (('building', 'room_number'),)
        
    def __str__(self):
        return self.building+' '+self.room_number
    
class Department(models.Model):
    dept_name = models.CharField(primary_key=True, max_length=20)
    building = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.dept_name
        
class Instructor(models.Model):
    bloodGroupList={
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('O+','O+'),
        ('O-','O-'),
    }
    user= models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    instructorId = models.CharField(primary_key=True, max_length=13)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=20,null=True, blank=True)
    dept_name = models.ForeignKey(Department, models.CASCADE, db_column='i_dept_name', blank=True, null=True)
    img = models.ImageField(null=True,upload_to='pics',default='DefaultProfilePic.jpg')
    email=models.EmailField(null=True, blank=True,max_length=254)
    bloodGroup= models.CharField(max_length=3,null=True, blank=True,choices=bloodGroupList)
    presentAddress = models.CharField(max_length=60,null=True,blank=True)
    phoneNumber = models.CharField(max_length=14,null=True,blank=True)
    
    def __str__(self):
        return self.firstName+'('+self.instructorId+')'

class Student(models.Model):
    bloodGroupList={
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('O+','O+'),
        ('O-','O-'),
    }
    user= models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    studentId = models.CharField(primary_key=True, max_length=13) 
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20,null=True, blank=True)
    dept_name = models.ForeignKey(Department, models.CASCADE, db_column='dept_name', blank=True, null=True)
    img = models.ImageField(null=True,upload_to='pics',default='DefaultProfilePic.jpg')
    email=models.EmailField(null=True, blank=True,max_length=254)
    tot_cred = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    bloodGroup= models.CharField(max_length=3,null=True, blank=True,choices=bloodGroupList)
    presentAddress = models.CharField(max_length=60,null=True,blank=True)
    phoneNumber = models.CharField(max_length=14,null=True,blank=True)

    def __str__(self):
        return self.firstName+str(self.lastName)+'('+self.studentId+')'

class Advisor(models.Model):
    s = models.OneToOneField('Student', models.CASCADE, db_column='s_ID', primary_key=True) 
    i = models.ForeignKey('Instructor', models.CASCADE, db_column='i_ID', blank=True, null=True)

    def __str__(self):
        return self.i.instructorId


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=8)
    title = models.CharField(max_length=50, blank=True, null=True)
    dept_name = models.ForeignKey('Department', models.CASCADE, db_column='dept_name', blank=True, null=True)
    credits = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return self.course_id

class TimeSlot(models.Model):
    time_slot_id = models.CharField(max_length=10)
    day = models.CharField(max_length=2)
    start_hr = models.CharField(max_length=2)
    start_min = models.CharField(max_length=2)
    end_hr = models.CharField(max_length=2)
    end_min = models.CharField(max_length=2)

    class Meta:
        unique_together = (('time_slot_id', 'day', 'start_hr', 'start_min'),)
    
    def __str__(self):
        return self.time_slot_id

class Section(models.Model):
    sem_list={
        ('Summer','Summer'),
        ('Fall','Fall'),
        ('Spring','Spring')
    }
    course = models.ForeignKey(Course, models.CASCADE,db_column='course_id')
    secId = models.CharField(max_length=8)
    semester = models.CharField(max_length=6,choices=sem_list)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    classroom = models.ForeignKey(Classroom, models.CASCADE)
    timeSlot = models.ForeignKey(TimeSlot,models.CASCADE)
    instructor = models.ForeignKey(Instructor, models.DO_NOTHING)
    class Meta:
        unique_together = (('course', 'secId', 'semester', 'year','timeSlot'),
                           ('classroom','semester','year','timeSlot'),
                            ('semester','year','timeSlot','course'),
                            ('semester','year','timeSlot','instructor'),
                            ('secId','course','semester', 'year')
                           )
    def __str__(self):
        return self.course.course_id+'('+self.secId+')'+'('+self.semester+ ' -'+str(self.year)+')'
        
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
        ('F','F'),
    }
    takes_id = models.ForeignKey(Student, models.CASCADE, db_column='studentId')
    grade = models.CharField(max_length=2, blank=True, null=True,choices=grade_list)
    section=models.OneToOneField(Section,models.CASCADE)
                  
    def __str__(self):
        return self.takes_id.firstName+'('+self.section.course_id+' '+self.section.semester+'-'+str(self.section.year)+')'
  
class Prereq(models.Model):
    course = models.ForeignKey(Course, models.CASCADE,related_name='CourseId')
    prereq = models.ForeignKey(Course, models.CASCADE,related_name='PreReqId')
    def __str__(self):
        return self.course_id +' <-- '+self.prereq.course_id
    class Meta:
        unique_together = (('course', 'prereq'),)
