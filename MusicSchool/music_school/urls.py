from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from . import views

urlpatterns = [
	path('', views.index, name='index'),
   	path('studentregistration/', views.studentRegister, name = 'studentregistration'),
   	path('studentregistered/', views.studentRegistered, name = 'studentregistered'),
	url(r'^login/$', auth_views.login, {'template_name': 'studentRegistration.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
	url(r'^signup/$', views.studentRegister, name='signup'),
]