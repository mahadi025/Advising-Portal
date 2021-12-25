from django.db import models

from accounts .models import Student,Course,Section

class AdvisingStudent(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    # advisingDay = models.CharField(max_length=2,null=True,blank=True)
    # startHour = models.CharField(max_length=2,null=True,blank=True)
    # startMinute = models.CharField(max_length=2,null=True,blank=True)
    # endHour = models.CharField(max_length=2,null=True,blank=True)
    # endMinute = models.CharField(max_length=2,null=True,blank=True)
    
    def __str__(self):
        return self.student.firstName+' '+str(self.student.lastName)+'('+self.student.studentId+')'
    
class AdvisingSlip(models.Model):
    student=models.OneToOneField(AdvisingStudent,on_delete=models.CASCADE)
    section=models.OneToOneField(Section, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.student.studentId+' '+self.section.semester+' '+self.section.year