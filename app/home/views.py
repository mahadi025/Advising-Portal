from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

year = settings.YEAR
semester = settings.SEMESTER


@login_required(login_url="login")
def home(request):
    context = {"year": year, "semester": semester}
    return render(request, "home/home.html", context)
