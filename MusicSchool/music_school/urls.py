from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from . import views

urlpatterns = [
   	url(r'^login/$', auth_views.login, {'template_name': 'studentRegistration.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': 'index'}, name='logout'),
	url(r'^signup/$', views.student_register, name='signup'),
	url(r'^booking/$', views.create_a_booking, name='booking'),
	url(r'^index/$', views.Index.as_view(), name='index'),
	url(r'^profile/$', views.ViewProfile.as_view(), name='profile'),
	url(r'^update/(?P<slug>[\-\w]+)/$', views.UpdateProfile.as_view(), name='update'),
	url(r'^confirm/$', views.confirm_booking, name='confirm'),
	url(r'^apply/$', views.form_upload, name='apply'),
	url(r'^instrument/$', views.instrument_request, name='instrument'),
]