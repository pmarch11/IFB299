from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import StudentRegistrationForm
from .models import UserProfile
from .models import bookingsModel

# Create your views here.
#@login_required
def index(request):
	return render(request,'index.html')

def student_register(request):
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
			if(user is not None):
				return redirect("index")

	else:
		form = StudentRegistrationForm()

	return render(request, 'studentRegistration.html', {'form': form})

def student_registered(request):
	return HttpResponse("You're now a registered student!")

def student_booking(request):
	return render(request,'makebooking.html')

def view_profile(request):
	return render(request,'profile.html')

def create_booking(request):
	if request.method == 'POST':
		bookings = bookingsModel()
		bookings.studentID = 1
		bookings.teacherID = 1
		bookings.startingDate = request.POST.get('dateSelect')
		bookings.startingTime = request.POST.get('dateSelect')
		bookings.lessonDuration = request.POST.get('dateSelect')
		bookings.instrumentFocus = request.POST.get('dateSelect')
		bookings.isRecurring = request.POST.get('dateSelect')
		bookings.lessonRepeat = request.POST.get('dateSelect')
		bookings.secondaryLessonDay = request.POST.get('dateSelect')
		bookings.secondaryLessonTime = request.POST.get('dateSelect')
		bookings.tertiaryLessonDay = request.POST.get('dateSelect')
		bookings.tertiaryLessonTime = request.POST.get('dateSelect')

