from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.template import Context, loader

from .forms import StudentRegistrationForm
from .models import UserProfile, bookingsModel

# Create your views here.
class Index(View):
	template_name = 'index.html'

	def get(self,request):
		return render(request,self.template_name)

class ViewProfile(View):
	model = UserProfile
	template_name = 'profile.html'

	def get(self,request):
		number = request.user.profile.phone_number
		#dob = request.user.profile.dob
		return render(request,self.template_name, {'number': number,})

class UpdateProfile(UpdateView):
	model = UserProfile
	fields = ['phone_number',]
	template_name = 'update.html'
	slug_field = 'phone_number'
	slug_url_kwarg = 'slug'

	def get(self,request,**kwargs):
		return redirect("profile")

def student_register(request):
	if request.method == 'POST':
		form = StudentRegistrationForm(request.POST)
		if form.is_valid():
			#create django user
			user = form.save(commit = False)
			user.save()
			#create profile (django custom model)
			newProfile = UserProfile.objects.get(user = user)
			#newProfile.DOB = form.cleaned_data.get('dob')
			newProfile.phone_number = form.cleaned_data.get('phone_number')
			newProfile.save()
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

def confirm_booking(request):
	return render(request,'bookingconfirmation.html')

def create_booking(request):
	if request.method == 'POST':
		bookings = bookingsModel()
		bookings.studentID = 1
		bookings.teacherID = 1
		bookings.startingDate = request.POST.get('dateSelect')
		bookings.startingTime = request.POST.get('timeSelect')
		bookings.lessonDuration = request.POST.get('durationSelect')
		bookings.instrumentFocus = request.POST.get('instrumentSelect')
		bookings.isRecurring = request.POST.get('recurringBox')
		bookings.lessonRepeat = request.POST.get('repeatedLessonSelect')
		bookings.secondaryLessonDay = request.POST.get('secondDaySelect')
		bookings.secondaryLessonTime = request.POST.get('secondTimeSelect')
		bookings.tertiaryLessonDay = request.POST.get('thirdDaySelect')
		bookings.tertiaryLessonTime = request.POST.get('thirdTimeSelect')

		bookings.save()

		return render(request, 'bookingconfirmation.html')

	else:
		return render(request, 'makebooking.html')

