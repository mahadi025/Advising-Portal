from django.contrib import admin
from .models import *

admin.site.register(Department)
admin.site.register(ClassRoom)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Takes)
admin.site.register(Prereq)

