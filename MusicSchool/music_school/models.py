from django.db import models

# Create your models here.
class User(models.Model):
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
