from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect, render_to_response,get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.template import Context, loader
from django.contrib.auth.models import User
from django.db.models import F
import datetime

from .forms import StudentRegistrationForm, bookingFormInitial, BookingFormDetail, resumeForm, instrumentForm
from .models import UserProfile, bookingModelInitial, bookingModelDetail, instrumentStockModel, TeacherProfile


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
		file = request.user.profile.file
		#dob = request.user.profile.dob
		return render(request,self.template_name, {'number': number, 'file': file})

class ViewTProfile(View):
	model = TeacherProfile
	template_name = 'tprofile.html'

	def get(self,request,teacher):
		teacherUser = User.objects.filter(username = teacher)
		for e in teacherUser:
			print(e.username)
		searchUser = get_object_or_404(User, username = teacher)
		teacherInfo = TeacherProfile.objects.filter(user = searchUser)
		return render(request,self.template_name, {'teacherUser': teacherUser, 'teacherInfo': teacherInfo})


class UpdateProfile(UpdateView):
	user = User
	model = UserProfile
	fields = ['phone_number',]
	template_name = 'update.html'
	slug_field = 'user'
	slug_url_kwarg = 'slug'

	def get(self,request,**kwargs):
		self.object = UserProfile.objects.get(id=self.kwargs['id'])
		context = self.get_context_data(object=self.object)
		return render(request, 'template.html', {"phone_number": phone_number, "file": file})
	
	def get_object(self, queryset=None):
		obj = UserProfile.objects.get(id=self.kwargs['id'])
		return obj

def student_register(request):
	if request.method == 'POST':
		form = StudentRegistrationForm(request.POST, request.FILES)
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
	if request.method == 'POST':
		form = BookingFormDetail(request.POST)
		if form.is_valid():
			bookingDetail = form.save()
			BOOKingID = bookingModelInitial.objects.latest('bookingID')
			bookingDetail.bookingID = BOOKingID
			bookingDetail.save()
			return HttpResponse("Booked")
	else:
		form = BookingFormDetail()

	return render(request, 'bookingconfirmation.html', { 'form': form, 'booking': bookingModelInitial.objects.latest('bookingID') })
	#bookingModelInitial.objects.order_by('bookingID')[0]


def create_a_booking(request):
	if request.method == 'POST':
		form = bookingFormInitial(request.POST)
		if form.is_valid():
			bookingInitial = form.save()
			bookingInitial.studentUsername = request.user.username
			bookingInitial.save()

			return redirect("confirm")
	else:
		form = bookingFormInitial()

	return render(request, 'makeabooking.html', { 'form': form })



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
