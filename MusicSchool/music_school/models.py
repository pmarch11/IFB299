from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save

# Create your models here.

#extends Django user model
class UserProfile(models.Model):
	user = models.OneToOneField(
		User,
		on_delete='cascade',
		related_name='profile'
	)
	#dob = models.DateField("Date of Birth")
	phone_number = models.IntegerField(max_length = 10,default="0410000000")
	file = models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username

def ProfileCreation(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user = kwargs['instance'])
post_save.connect(ProfileCreation, sender = User)

# class TeacherProfile(models.Model):
# 	user = models.OneToOneField(
# 		User,
# 		on_delete='cascade',
# 		related_name='profile'
# 	)

class TeacherProfile(models.Model):
	user = models.OneToOneField(
		User,
		on_delete='cascade',
		related_name='Tprofile'
	)
	qualifications = models.TextField()
	instrument_skill = models.TextField()
	language_skill = models.TextField()
	phone_number = models.IntegerField(max_length = 10,default="0410000000")
	file = models.ImageField(upload_to='media/teacherphoto/')
	uploaded_at = models.DateTimeField(auto_now_add=True)





class OldUserModel(models.Model):
	STUDENT = 'S'
	TEACHER = 'T'
	ADMIN = 'A'
	OWNER = 'O'
	NEW = 'New'
	OLD = 'Old'

	ROLE_CHOICES = (
		(STUDENT, 'Student'),
		(TEACHER, 'Teacher'),
		(ADMIN, 'Administrator'),
		(OWNER, 'Owner'),
	)
	STUDENT_TYPE_CHOICES = (
		(NEW, 'New'),
		(OLD, 'Old'),
	)

	user_id = models.AutoField(primary_key = True)
	Role = models.CharField(
		max_length = 1,
		choices = ROLE_CHOICES,
		default = STUDENT,
	) 
	First_Name = models.CharField(max_length = 20)
	Last_Name = models.CharField(max_length = 20)
	DOB = models.DateField("Date of Birth")
	Phone_Number = models.PositiveIntegerField(max_length = 10)
	Qualifications = models.TextField()
	Email_Address = models.EmailField(max_length = 50)
	Facebook_ID = models.URLField(max_length = 75)
	#TODO: change this to drop-down
	Languages_Spoken = models.TextField()
	#language_skill = 
	Instruments_Played = models.TextField()
	#instrument_skill
	Parent_Name = models.CharField(max_length = 50)
	Parent_Email = models.EmailField(max_length = 50)
	parent_phoneNum = models.PositiveIntegerField("Parent's phone number", max_length = 10)
	Student_Type = models.CharField(
		max_length = 3,
		choices = STUDENT_TYPE_CHOICES,
		default = NEW
	)



class bookingModelInitial(models.Model):

	bookingID = models.AutoField(primary_key=True)
	studentUsername = models.CharField(max_length=30)
	teacherUsername = models.CharField(max_length=30)
	recurringAmount = models.CharField(max_length=30)
	

class bookingModelDetail(models.Model):

	bookingDetailID = models.AutoField(primary_key=True)
	startingDate = models.DateField()
	startingTime = models.CharField(max_length = 10)
	lessonDuration = models.IntegerField(default=30)
	instrumentFocus = models.CharField(max_length = 30)
	bookingID = models.ForeignKey(bookingModelInitial, on_delete=models.CASCADE, blank=True, null=True) #needs to be changed to foreignkey
	
	secondaryLessonDay = models.CharField(null=True, max_length=20, blank=True)
	secondaryLessonTime = models.CharField(null=True, max_length=10, blank=True)
	tertiaryLessonDay = models.CharField(null=True, max_length=20, blank=True)
	tertiaryLessonTime = models.CharField(null=True, max_length=10, blank=True)

class resumeModel(models.Model):
	notes = models.CharField(max_length=255, blank=True)
	document = models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)

#for available stock
class instrumentStockModel(models.Model):
	instrumentType = models.CharField(primary_key=True, max_length=30)
	stock = models.IntegerField()
	hire_cost = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return self.instrumentType

#for student renting instrument
class instrumentRequestModel(models.Model): 
	requestID = models.AutoField(primary_key=True)
	instrumentType = models.ForeignKey(instrumentStockModel, on_delete=models.CASCADE)
	studentUsername = models.CharField(max_length=30)
	return_date = models.DateField()