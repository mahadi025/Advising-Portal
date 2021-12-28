from django.db import models

from accounts .models import Student,Course,Section

class AdvisingStudent(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    # advisingDay = models.CharField(max_length=2,null=True,blank=True)
    # startHour = models.CharField(max_length=2,null=True,blank=True)
    # startMinute = models.CharField(max_length=2,null=True,blank=True)
    # endHour = models.CharField(max_length=2,null=True,blank=True)
    # endMinute = models.CharField(max_length=2,null=True,blank=True)
    creditsTaken=models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True,default=0.0,editable=True)
    
    def __str__(self):
        return self.student.firstName+' '+str(self.student.lastName)+'('+self.student.studentId+')'
    
class AdvisingSlip(models.Model):
    advisingStudent=models.ForeignKey(AdvisingStudent,on_delete=models.CASCADE)
    section=models.OneToOneField(Section, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.advisingStudent.student.studentId+' '+self.section.semester+' '+str(self.section.year)