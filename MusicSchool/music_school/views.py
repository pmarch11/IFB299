from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import StudentRegistrationForm
from .models import UserProfile

# Create your views here.
#@login_required
def index(request):
	return render(request,'index.html')

def studentRegister(request):
	if request.method == 'POST':
		form = StudentRegistrationForm(request.POST)
		if form.is_valid():
			date_of_birth = form.cleaned_data.get('DOB')
			mobile = form.cleaned_data.get('Phone_Number')
			user = form.save(commit = False)
			user.save()
			UserProfile.objects.create(user=user,DOB=date_of_birth,Phone_Number=mobile)
			login(request,user)
			#redirect to new URL
			return redirect(index)
	else:
		form = StudentRegistrationForm()

	return render(request, 'studentRegistration.html', {'form': form})

def studentRegistered(request):
	return HttpResponse("You're now a registered student!")