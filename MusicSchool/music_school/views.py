from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.http import HttpResponse

from .forms import StudentRegistrationForm

# Create your views here.
@login_required
def index(request):
	return render(request,'index.html')

def studentRegister(request):
	if request.method == 'POST':
		form = StudentRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			#user.refresh_from_db()

			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username = username, password = raw_password)
			login(request,user)
			#redirect to new URL
			return redirect(index)
	else:
		form = StudentRegistrationForm()

	return render(request, 'studentRegistration.html', {'form': form})

def studentRegistered(request):
	return HttpResponse("You're now a registered student!")