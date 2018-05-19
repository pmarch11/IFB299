from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect, render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.template import Context, loader
from django.contrib.auth.models import User
from django.db.models import F

from .forms import StudentRegistrationForm, BookingForm, BookingFormRecurring, resumeForm, instrumentForm
from .models import UserProfile, bookingModel, bookingModelRecurring, instrumentStockModel

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

def confirm_booking(request):
	template = 'bookingconfirmation.html'
	context = {'booking': bookingModel.objects.order_by('bookingID')[0], 'bookingRecurring': bookingModelRecurring.objects.order_by('bookingID')[0]}
	return render_to_response(template, context)


def create_a_booking(request):
	if request.method == 'POST':
		form = BookingForm(request.POST)
		form2 = BookingFormRecurring(request.POST)
		if form.is_valid() and form2.is_valid():
			booking = form.save()
			booking.studentUsername = request.user.username
			booking.save()

			bookingRecurring = form2.save()
			bookingRecurring.bookingID = bookingModel.objects.get(bookingID=booking.bookingID)
			
			bookingRecurring.save()
			return redirect("confirm")
	else:
		form = BookingForm()
		form2 = BookingFormRecurring()

	return render(request, 'makeabooking.html', { 'form': form, 'form2': form2})

#class view_booking(View):
#	model = bookingModel #add bookingModelrecurring
#	template_name = 'makeabooking.html'
#
#	def get(self,request):
#		booking = request.booking
#		return render(request,self.template_name, {'booking': booking,})

#def view_booking(request):
#	template = 'bookingconfirmation.html'
#	context = {'booking': bookingModel.objects.get(instrumentType=) }



def form_upload(request):
	if request.method == 'POST':
		form = resumeForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse("Thank you for your submission, we will contact you through email")
	else:
		form = resumeForm()
	return render(request, 'resume_upload.html', { 'form': form})

def instrument_request(request):
	if request.method == 'POST':
		form = instrumentForm(request.POST, request.FILES)
		InstrumentStock = instrumentStockModel.objects.get(pk=form.data['instrumentType'])
		if form.is_valid():
			# if there is at least 1 selected instruent
			if InstrumentStock.stock > 0:
				#decrement stock
				InstrumentStock.stock = F('stock') - 1
				InstrumentStock.save()
				#save form and tell user it was successful
				instrumentRequest = form.save()
				instrumentRequest.studentUsername = request.user.username
				instrumentRequest.save()
				return HttpResponse("Thank you for your rental, come to Mika's music school in person to collect your instrument")
			else:
				return HttpResponse("Instrument is currently out of stock")
			
	else:
		form = instrumentForm()
	return render(request, 'instrumentHire.html', { 'form': form})
