from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import bookingModelInitial, bookingModelDetail, resumeModel, instrumentRequestModel, instrumentStockModel, feedbackModel
import datetime

TimeCHOICES = (
		('',''),
		('10:30am', '10:30am'),
		('11:00am', '11:00am'),
		('11:00am', '11:00am'),
		('11:00am', '11:00am'),
		('11:00am', '11:00am'),
		)

TeacherCHOICES = (
	('',''),
	('Clint Stevens', 'Clint Stevens'),
	('Mika Jones', 'Mika Jones'),
	('Doug Kelly', 'Doug Kelly'),
	)

DURATION_CHOICES = (
	('',''),
	(30, '30 Minutes'),
	(60, '60 Minutes'),
	)

	

LESSON_DAY_CHOICES = (
	('',''),
	(1, 'Monday'),
	(2, 'Tuesday'),
	(3, 'Wednesday'),
	(4, 'Thursday'),
	(5, 'Friday'),
)

REPEATS_CHOICES = (
	('',''),
	('Weekly', 'Weekly'),
	('Fornightly', 'Fornightly'),
	('Twice per Week', 'Twice per Week'),
	('Thrice per Week', 'Thrice per Week'),
)

INSTRUMENTS_CHOICES = (
	('',''),
	('Trombone', 'Trombone'),
	('Tuba', 'Tuba'),
	('Saxophone', 'Saxophone'),
	)

class DateInput(forms.DateInput):
	input_type = 'date'

class StudentRegistrationForm(forms.Form, UserCreationForm):
	fType = "register"

	username = forms.CharField(max_length=20)
	first_name = forms.CharField(label = 'First Name', max_length = 20)
	last_name = forms.CharField(label = 'Last Name', max_length = 20)
	#dob = forms.DateField(label = 'Date of Birth')
	phone_number = forms.IntegerField(label = 'Mobile Number')
	email = forms.EmailField(label = 'Email Address')
	file = forms.FileField(label = 'Profile Photo')
	# Qualifications = forms.CharField(label = 'Qualifications')
	# Facebook_ID = forms.URLField(label = 'Facebook ID', max_length = 75)
	# #TODO: change this to drop-down
	# Languages_Spoken = forms.CharField(label = 'Languages Spoken')
	# #language_skill = 
	# Instruments_Played = forms.CharField(label = 'Instruments Played')
	# #instrument_skill
	# Parent_Name = forms.CharField(label = 'Parent Name', max_length = 50)
	# Parent_Email = forms.EmailField(label = 'Parent Email')
	# parent_phoneNum = forms.IntegerField(label = 'Parent phone number')



	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2','file')


class bookingFormInitial(forms.ModelForm):
	teacherUsername = forms.CharField(label = 'Select teacher', widget=forms.Select(choices=TeacherCHOICES))
	recurringAmount = forms.CharField(label = "How often?", widget=forms.Select(choices=REPEATS_CHOICES))

	class Meta:
		model = bookingModelInitial
		fields = ('teacherUsername', 'recurringAmount')
		

class BookingFormDetail(forms.ModelForm):
	startingDate = forms.DateInput()
	startingTime = forms.CharField(label = 'Available starting times', widget=forms.Select(choices=TimeCHOICES))
	lessonDuration = forms.CharField(label = 'Lesson length', widget=forms.Select(choices=DURATION_CHOICES))
	instrumentFocus = forms.CharField(label = 'Which instrument?', widget=forms.Select(choices=INSTRUMENTS_CHOICES))
	
	secondaryLessonDay = forms.CharField(label = "Secondary lesson day", widget=forms.Select(choices=LESSON_DAY_CHOICES), required=False)
	secondaryLessonTime = forms.CharField(label = "Secondary lesson time", widget=forms.Select(choices=TimeCHOICES), required=False)
	tertiaryLessonDay = forms.CharField(label = "Third lesson day", widget=forms.Select(choices=LESSON_DAY_CHOICES), required=False)
	tertiaryLessonTime = forms.CharField(label = "Third lesson time", widget=forms.Select(choices=TimeCHOICES), required=False)

	# function to check return date in the future
	def clean_startingDate(self):
		date = self.cleaned_data.get("startingDate")
		if date < datetime.date.today():
			raise forms.ValidationError("The starting date must be in the future!")
		return date


	class Meta:
		model = bookingModelDetail
		fields = ('startingDate', 'startingTime', 'lessonDuration', 'instrumentFocus', 'secondaryLessonDay', 'secondaryLessonTime', 'tertiaryLessonDay', 'tertiaryLessonTime')
		widgets = {
			'startingDate': DateInput()
		}
class resumeForm(forms.ModelForm):
	notes = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20",}))

	class Meta:
		model = resumeModel
		fields = ('document', 'notes', )

class instrumentForm(forms.ModelForm):
	#instrumentType = forms.CharField(label = 'Which type of instrument?', widget=forms.Select(choices=INSTRUMENTS_CHOICES))
	instrumentType = forms.ModelChoiceField(
		label = "Type of instrument",
		queryset=instrumentStockModel.objects.all(),
		widget=forms.Select(attrs={'class': 'instrumentType'}),
	)
	return_date = forms.DateInput()


	# function to check return date in the future
	def clean_return_date(self):
		date = self.cleaned_data.get("return_date")
		if date < datetime.date.today():
			raise forms.ValidationError("The date of return must be in the future!")
		return date


	class Meta:
		model = instrumentRequestModel
		fields = ( 'instrumentType', 'return_date')
		widgets = {
			'return_date': DateInput()
		}

class feedbackForm(forms.ModelForm):
	teacherUsername = forms.CharField(label="Select teacher to give feedback", widget=forms.Select(choices=TeacherCHOICES))
	feedbackDescription = forms.CharField(label="Leave feedback here", widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20",}))


	class Meta:
		model = feedbackModel
		fields = ( 'teacherUsername', 'feedbackDescription')