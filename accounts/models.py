from django.db import models

class student_info(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    student_id=models.CharField(max_length=13)
    password =models.CharField(max_length=20)
    img= models.ImageField(upload_to='pics')