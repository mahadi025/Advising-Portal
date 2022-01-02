from django.db import models
from django.core.exceptions import ValidationError
from accounts .models import Student,Course,Section,TimeSlot

class AdvisingStudent(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    creditsTaken=models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True,default=0.0,editable=True)
    sundayClass=models.DecimalField(max_digits=1, decimal_places=0,null=True,blank=True,default=0.0,editable=True)
    mondayClass=models.DecimalField(max_digits=1, decimal_places=0,null=True,blank=True,default=0.0,editable=True)
    tuesdayClass=models.DecimalField(max_digits=1, decimal_places=0,null=True,blank=True,default=0.0,editable=True)
    wednesdayClass=models.DecimalField(max_digits=1, decimal_places=0,null=True,blank=True,default=0.0,editable=True)
    thursdayClass=models.DecimalField(max_digits=1, decimal_places=0,null=True,blank=True,default=0.0,editable=True)
    def __str__(self):
        return self.student.firstName+' '+str(self.student.lastName)+'('+self.student.studentId+')'
    
class AdvisingSlip(models.Model):
    advisingStudent=models.ForeignKey(AdvisingStudent,on_delete=models.CASCADE)
    section=models.ForeignKey(Section, on_delete=models.CASCADE)
    course=models.CharField(max_length=8,null=True, blank=True)
    courseTaken=models.OneToOneField(Course, on_delete=models.CASCADE,null=True,blank=True)
    semester = models.CharField(max_length=6,null=True,blank=True)
    year = models.DecimalField(max_digits=4, decimal_places=0,null=True,blank=True)
    timeSlot=models.ForeignKey(TimeSlot, on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
        unique_together=(('course','semester', 'year','advisingStudent','section','timeSlot'))
    def __str__(self):
        return self.advisingStudent.student.studentId+' '+self.section.course.course_id+' '+self.section.semester+' '+str(self.section.year)