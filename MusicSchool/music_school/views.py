from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentRegistrationForm

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're at the music school index.")

def studentRegister(request):
	if request.method == 'POST':
		form = StudentRegistrationForm(request.POST)
		if form.is_valid():
			#redirect to new URL
			return HttpResponse(response)
	else:
		form = StudentRegistrationForm()

	return render(request, 'studentRegistration.html', {'form': form})

def studentRegistered(request):
	return HttpResponse("You're now a registered student!")