# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

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
    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.dept_name
        
class Instructor(models.Model):
    instructor_id = models.CharField(primary_key=True, max_length=13)
    name = models.CharField(max_length=50)
    dept_name = models.ForeignKey(Department, models.CASCADE, db_column='i_dept_name', blank=True, null=True)

    def __str__(self):
        return self.name+'('+self.dept_name.dept_name+')'

class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=13) 
    name = models.CharField(max_length=20)
    dept_name = models.ForeignKey(Department, models.CASCADE, db_column='dept_name', blank=True, null=True)
    tot_cred = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return self.name+'('+self.student_id+')'

class Advisor(models.Model):
    s = models.OneToOneField('Student', models.CASCADE, db_column='s_ID', primary_key=True) 
    i = models.ForeignKey('Instructor', models.CASCADE, db_column='i_ID', blank=True, null=True)

    def __str__(self):
        return self.i.name


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
    start_hr = models.DecimalField(max_digits=2, decimal_places=0)
    start_min = models.DecimalField(max_digits=2, decimal_places=0)
    end_hr = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    end_min = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

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
    sec_id = models.CharField(max_length=8)
    semester = models.CharField(max_length=6,choices=sem_list)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    classroom = models.ForeignKey(Classroom, models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, models.DO_NOTHING,null=True,blank=True)
    class Meta:
        unique_together = (('course', 'sec_id', 'semester', 'year','time_slot'),
                           ('classroom','time_slot','semester','year'),
                           )
    def __str__(self):
        return self.course.course_id+'('+self.sec_id+')'+'('+self.semester+ ' -'+str(self.year)+')'
 
class Teaches(models.Model):
    teaches_id = models.ForeignKey(Instructor, models.CASCADE, db_column='instructor_id')  
    # course = models.ForeignKey(Section, models.DO_NOTHING,db_column='course',related_name='teaches_course')
    # sec = models.ForeignKey(Section, models.DO_NOTHING,db_column='sec_id',related_name='teaches_sec')
    # semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='semester',related_name='teaches_semester')
    # year = models.ForeignKey(Section, models.DO_NOTHING, db_column='year',related_name='teaches_year')
    section = models.OneToOneField(Section, models.CASCADE,null=True,blank=True)
    def __str__(self):
         return self.teaches_id.instructor_id+'-'+self.section.course_id+'('+self.section.sec_id+')'+'-'+self.section.semester+'-'+str(self.section.year)

class Takes(models.Model):
    takes_id = models.ForeignKey(Student, models.CASCADE, db_column='student_id')
    # course = models.OneToOneField(Section, models.DO_NOTHING,db_column='course', related_name='takes_course')
    # sec = models.OneToOneField(Section, models.DO_NOTHING,db_column='sec_id',related_name='takes_sec')
    # semester = models.OneToOneField(Section, models.DO_NOTHING, db_column='semester',related_name='takes_semester')
    # year = models.OneToOneField(Section, models.DO_NOTHING, db_column='year',related_name='takes_year')
    grade = models.CharField(max_length=2, blank=True, null=True)
    section=models.OneToOneField(Section,models.CASCADE,null=False,blank=True,primary_key=True)
    def __str__(self):
        return self.takes_id.name+'('+self.section.course.course_id+' '+self.section.semester+'-'+str(self.section.year)+')'
  
class Prereq(models.Model):
    course = models.ForeignKey(Course, models.CASCADE,related_name='CourseId')
    prereq = models.ForeignKey(Course, models.CASCADE,related_name='PreReqId')
    def __str__(self):
        return self.course_id +' <-- '+self.prereq.course_id
    class Meta:
        unique_together = (('course', 'prereq'),)



