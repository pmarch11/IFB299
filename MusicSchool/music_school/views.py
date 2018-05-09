from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.template import Context, loader

from .forms import StudentRegistrationForm, BookingsForm, BookingsFormRecurring, resumeForm
from .models import UserProfile, bookingsModel, bookingsModelRecurring

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
		form = BookingsForm(request.POST)
		form2 = BookingsFormRecurring(request.POST)
		if form.is_valid() and form2.is_valid():
			booking = form.save()
			bookingRecurring = form2.save()
			return redirect("confirm")
	else:
		form = BookingsForm()
		form2 = BookingsFormRecurring()

	return render(request, 'makebooking.html', { 'form': form, 'form2': form2})

def form_upload(request):
	if request.method == 'POST':
		form = resumeForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse("Thank you for your submission, we will contact you through email")
	else:
		form = resumeForm()
	return render(request, 'resume_upload.html', { 'form': form})