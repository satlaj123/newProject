from django.conf.urls import url, include, patterns
from form.views import *
# from django.conf import settings
urlpatterns = [
	url(r'^registerShow',registerShow, name='registration page'),
	url(r'^register',register, name='register page'),
	url(r'^homepage',homepage, name='homepage page'),
	url(r'^confirmation/',confirmation, name='confirmation page'),
	url(r'^my_login/',my_login, name='login page'),
	url(r'^home/',home, name='home page'),
	url(r'^profile/',profile, name='profile page'),
	url(r'^contact/',contact, name='contact page'),
	url(r'^sendmessage/',sendmessage, name='sendmessage page'),
	url(r'^update_profile/',update_profile, name='update_profile page'),
	url(r'^aboutus/',about, name = 'about_us page'),
	url(r'^upload_file', upload_file, name = 'upload your file'),
	]