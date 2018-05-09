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



class bookingsModel(models.Model):

	DURATION_CHOICES = (
		(30, '30 Minutes'),
		(60, '60 Minutes'),
	)

	REPEATS_CHOICES = (
		(1, 'Weekly'),
		(0.5, 'Fornightly'),
		(2, 'Twice per Week'),
		(3, 'Thrice per Week'),
	)

	LESSON_DAY_CHOICES = (
		(1, 'Monday'),
		(2, 'Tuesday'),
		(3, 'Wednesday'),
		(4, 'Thursday'),
		(5, 'Friday'),
	)

	bookingID = models.AutoField(primary_key=True)
	studentID = models.IntegerField() #needs to be changed to foreignkey
	teacherID = models.IntegerField() #needs to be changed to foreignkey
	startingDate = models.DateField()
	startingTime = models.TimeField()
	lessonDuration = models.IntegerField(choices=DURATION_CHOICES, default=30)
	instrumentFocus = models.CharField(max_length = 30)
	isRecurring = models.BooleanField(default=False)
	#if recurring
	lessonRepeat = models.CharField(choices=REPEATS_CHOICES, default=None, max_length=20)
	secondaryLessonDay = models.CharField(choices=LESSON_DAY_CHOICES, default=None, max_length=20)
	secondaryLessonTime = models.TimeField(default=None)
	tertiaryLessonDay = models.CharField(choices=LESSON_DAY_CHOICES, default=None, max_length=20)
	tertiaryLessonTime = models.TimeField(default=None)

	




