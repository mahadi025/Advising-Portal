from django.shortcuts import render, redirect
from .forms import *
from accounts.models import *
def advising(request):
    form=createAdvisingSlip()
    offeredCourses=Section.objects.filter(year=2021,semester='Summer')
    if request.method == 'POST':
        form=createAdvisingSlip(request.POST)
        if form.is_valid:
            form.save()
        return redirect('advising')
    contex={'form':form,'offeredCourses':offeredCourses}
    return render(request,'advising.html',contex)