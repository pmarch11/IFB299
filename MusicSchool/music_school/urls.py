from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from . import views

urlpatterns = [
	path('', views.index, name='index'),
   	path('studentregistration/', views.student_register, name = 'studentregistration'),
   	path('studentregistered/', views.student_registered, name = 'studentregistered'),
	url(r'^login/$', auth_views.login, {'template_name': 'studentRegistration.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': 'index'}, name='logout'),
	url(r'^signup/$', views.student_register, name='signup'),
	url(r'^booking/$', views.student_booking, name='booking'),
	url(r'^index/$', views.index, name='index'),
	url(r'^profile/$', views.view_profile, name='profile'),
	url(r'^confirm/$', views.confirm_booking, name='confirm')
]