from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user,allowed_users


@login_required(login_url='login')
# @allowed_users(allowed_roles=['student'])
def home(request):
    return render(request, 'home.html')

