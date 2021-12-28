from django.shortcuts import render, redirect,HttpResponse
from .forms import *
from accounts.models import *
from django.forms import inlineformset_factory
def advising(request):
    form=createAdvisingSlip()
    offeredCourses=Section.objects.filter(year=2019,semester='Summer')
    if request.method == 'POST':
        form=createAdvisingSlip(request.POST)
        if form.is_valid:
            form.save()
        return redirect('advising')
    contex={'form':form,'offeredCourses':offeredCourses}
    return render(request,'advising.html',contex)

def create_advisingSlip(request):
    # form=inlineformset_factory(AdvisingStudent,AdvisingSlip,fields=['section'],)
    if request.method == 'POST':
        return HttpResponse("Added")
    contex={}
    
    return render(request,'AdvisingSlip.html',contex)

def add_course(request,pk):
    if AdvisingStudent.objects.filter(student=request.user.student):
        advisingStudent=AdvisingStudent.objects.get(student=request.user.student)
    else:
        advisingStudent=AdvisingStudent.objects.create(student=request.user.student)
        
    section=Section.objects.get(id=pk)
    print(section.course)
    AdvisingSlip.objects.create(advisingStudent=advisingStudent,section=section)
    return redirect('advising')