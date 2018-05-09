from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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