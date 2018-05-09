from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import bookingsModel, bookingsModelRecurring, resumeModel

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
	(1, 'Clint Stevens'),
	(2, 'Mika Jones'),
	(3, 'Doug Kelly'),
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
	(1, 'Weekly'),
	(0.5, 'Fornightly'),
	(2, 'Twice per Week'),
	(3, 'Thrice per Week'),
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
		fields = ('username','first_name','last_name','email','password1','password2',)


class BookingsForm(forms.ModelForm):
	studentUsername = 'test'
	startingDate = forms.DateInput()
	teacherID = forms.CharField(label = 'Select teacher', widget=forms.Select(choices=TeacherCHOICES))
	startingTime = forms.CharField(label = 'Available starting times', widget=forms.Select(choices=TimeCHOICES))
	lessonDuration = forms.CharField(label = 'For how long?', widget=forms.Select(choices=DURATION_CHOICES))
	instrumentFocus = forms.CharField(label = 'Which instrument?', widget=forms.Select(choices=INSTRUMENTS_CHOICES))

	class Meta:
		model = bookingsModel
		fields = ('teacherID', 'startingDate', 'startingTime', 'lessonDuration', 'instrumentFocus')
		widgets = {
			'startingDate': DateInput()
		}

class BookingsFormRecurring(forms.ModelForm):
	lessonRepeat = forms.CharField(label = "How often?", widget=forms.Select(choices=REPEATS_CHOICES), required=False)
	secondaryLessonDay = forms.CharField(label = "Secondary lesson day", widget=forms.Select(choices=LESSON_DAY_CHOICES), required=False)
	secondaryLessonTime = forms.CharField(label = "Secondary lesson time", widget=forms.Select(choices=TimeCHOICES), required=False)
	tertiaryLessonDay = forms.CharField(label = "Third lesson day", widget=forms.Select(choices=LESSON_DAY_CHOICES), required=False)
	tertiaryLessonTime = forms.CharField(label = "Third lesson time", widget=forms.Select(choices=TimeCHOICES), required=False)


	class Meta:
		model = bookingsModelRecurring
		fields = ('lessonRepeat', 'secondaryLessonDay', 'secondaryLessonTime', 'tertiaryLessonDay', 'tertiaryLessonTime')

class resumeForm(forms.ModelForm):
	notes = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20",}))


	class Meta:
		model = resumeModel
		fields = ('document', 'notes', )