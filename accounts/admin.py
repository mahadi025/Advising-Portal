from django.contrib import admin
from .models import *

admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Department)
admin.site.register(Advisor)
admin.site.register(Course)
admin.site.register(Prereq)
admin.site.register(TimeSlot)
admin.site.register(Takes)
admin.site.register(Section)
