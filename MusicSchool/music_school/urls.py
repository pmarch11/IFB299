from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
   	path('studentregistration/', views.studentRegister, name = 'studentregistration'),
   	path('studentregistered/', views.studentRegistered, name = 'studentregistered'),
]