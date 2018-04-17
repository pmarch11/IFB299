from django import forms

class StudentRegistrationForm(forms.Form):
	First_Name = forms.CharField(label = 'First Name', max_length = 20)
	Last_Name = forms.CharField(label = 'Last Name', max_length = 20)
	DOB = forms.DateField(label = 'Date of Birth')
	Phone_Number = forms.IntegerField(label = 'Mobile Number')
	Email_Address = forms.EmailField(label = 'Email Address')
	Qualifications = forms.CharField(label = 'Qualifications')
	Facebook_ID = forms.URLField(label = 'Facebook ID', max_length = 75)
	#TODO: change this to drop-down
	Languages_Spoken = forms.CharField(label = 'Languages Spoken')
	#language_skill = 
	Instruments_Played = forms.CharField(label = 'Instruments Played')
	#instrument_skill
	Parent_Name = forms.CharField(label = 'Parent Name', max_length = 50)
	Parent_Email = forms.EmailField(label = 'Parent Email')
	parent_phoneNum = forms.IntegerField(label = 'Parent phone number')