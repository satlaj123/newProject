from django.shortcuts import render, redirect
from random import randint
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

# Create your views here.
def registerShow(request):
	countryObjects = CountryMaster.objects.all()
	stateObjects = StateMaster.objects.all()
	cityObects = CityMaster.objects.all()
	blood_groupObjects = BloodGroupMaster.objects.all()
	genderObjects = GenderMaster.objects.all()

	return render(request,'register.html',{'countryObjects':countryObjects,'stateObjects':stateObjects,'cityObects':cityObects,'blood_groupObjects':blood_groupObjects,'genderObjects':genderObjects})


def confirmation(request):
	return render(request,'confirm.html')

def about(request):
	return render(request,'about.html')

def homepage(request):
	return render(request,'home.html')

def contact(request):
	return render(request,'contact.html')


def register(request):

	countryObjects = CountryMaster.objects.all()
	stateObjects = StateMaster.objects.all()
	cityObects = CityMaster.objects.all()
	blood_groupObjects = BloodGroupMaster.objects.all()
	genderObjects = GenderMaster.objects.all()


	response = {}
	if request.method =='POST':
		form = request.POST

		first_name = form['first_name']
		last_name = form['last_name']
		middle_name = form['middle_name']
		gender = GenderMaster.objects.get(name = form['gender'])
		blood_group = BloodGroupMaster.objects.get(name = form['blood_group'])
		country = CountryMaster.objects.get(name = form['country'])
		state = StateMaster.objects.get(name = form['state'])
		city = CityMaster.objects.get(name = form['city'])
		date_of_birth = form['dob']
		aadhar_no = form['adhar_number']
		password = form['password']
		# cpassword = form['confirm_password']
		mobile_number = form['mobile_number']
		email = form['email']
		address = form['address']
		pincode = form['pincode']
		activationToken = str(randomWithNDigits(8))
		lastUserId = User.objects.latest('id').id
		mrd = "MRD"+str(100000+lastUserId+1)

		user = User.objects.create_user(
			username = mrd,
			first_name = first_name,
			last_name = last_name,
			email = email,
			password = password,
			)
		newUser = Registration.objects.get_or_create(
			user = user,
			middle_name = middle_name,
			first_name = first_name,
			last_name = last_name,
			gender = gender,
			blood_group = blood_group,
			country = country,
			state = state,
			city = city,
			date_of_birth = date_of_birth,
			email = email,
			mobile_number = mobile_number,
			aadhar_no = aadhar_no,
			activationToken = activationToken,
			address = address,
			pincode = pincode,

			)
		return render(request,'confirm.html',{'mrd':mrd,'password':password,'user':user,'newUser':newUser})
	else:
		return render(request,'register.html',{'countryObjects':countryObjects,'stateObjects':stateObjects,'cityObects':cityObects,'blood_groupObjects':blood_groupObjects,'genderObjects':genderObjects})


@csrf_exempt
@login_required(login_url = '/my_login')
def my_login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username, password = password)
	if user is not None:
		if user.is_active:
			login(request,user)
			print('user is logged in')			
			# quer = user.email
			RegisterObject = Registration.objects.get(user = user)
			first_name = user.first_name
			# if RegisterObject.isProfileComplete:
			# 	return redirect('/dashboard/')

			# else:
			return redirect('/profile/')
		else:
			print('user is not logged in')
			messages.warning(request,"This account is not activated")
			return render(request,'login.html')

	else:
		print(4)
		messages.warning(request,"Invalid Credentials!!")
		return render(request,'login.html')

def home(request):
	return render(request,'login.html')

# def login(request):
# 	if request.method =='POST':
# 		form = request.POST
# 		print(form)
# 		try:
# 			username = User.objects.get(username = form['username'])
# 			print(1)
# 		except:
# 			try:
# 				username = User.objects.get(email = form['username'])
# 				print(username)
# 				print(2)
# 			except:
# 				message.warning(request,'Invalid Credential')
# 				return render(request,'login.html')
# 		try:
# 			user = authenticate(username = username,password = form['password'])
# 			if user is not None:
# 				if user.is_active:
# 					login(request,user)
# 					newUser = Registration.objects.get(user = user)
# 					return render(request,'dashboard.html',{'newUser':newUser})
					
# 				else:
# 					message.warning(request,"The account is disabled")
# 			else:
# 				print(4)
# 				message.warning(request,"Invalid Credential")
# 			return render(request,'login.html')
# 		except:
# 			print("user is not found, please create account")
# 			return render(request,'login.html')
# 	else:
# 		return render(request,'login.html')

# def resendOTP(request):
# 	response = {}
# 	if request.method =='POST':
# 		form = request.POST
# 		activationToken = str(randomWithNDigits(8))
# 		try:
# 			user = User.objects.get(username = form['mrd'])
# 			newUser = Registration.objects.get(user = user)
# 		except:
# 			message.warning(request,'Invalid MRD number')
# 			response['status'] = 2
# 			return JsonResponse(response)
# 		try:
# 			newUser.activationToken = activationToken
# 			newUser.save()
# 			response['status'] = 1
# 			return JsonResponse(response)
# 		except:
# 			response['status'] = 0
# 			return JsonResponse(response)

@csrf_exempt
@login_required(login_url = '/login')
def profile(request):

	countryObjects = CountryMaster.objects.all()
	stateObjects = StateMaster.objects.all()
	cityObects = CityMaster.objects.all()
	blood_groupObjects = BloodGroupMaster.objects.all()
	genderObjects = GenderMaster.objects.all()

	# response = {}
	user = request.user
	
	print(user)
	profileObjects = Registration.objects.get(user = user)

	return render(request,'profile.html',{'profileObjects':profileObjects, 'user':user,'countryObjects':countryObjects,'stateObjects':stateObjects,'cityObects':cityObects,'blood_groupObjects':blood_groupObjects,'genderObjects':genderObjects})

@csrf_exempt
@login_required(login_url = '/login')
def update_profile(request):
	response = {}
	user = request.user

	profileObjects = Registration.objects.get(user = user)
	# genderObjects = GenderMaster.objects.all()
	# blood_groupObjects = BloodGroupMaster.objects.all()
	countryObjects = CountryMaster.objects.all()
	stateObjects = StateMaster.objects.all()
	cityObjects = CityMaster.objects.all()
	# nameObjects = Registration.objects.all()
	if request.method == 'POST':
		form = request.POST


		genderObjects = GenderMaster.objects.get(name = form['gender'])
		blood_Objects = BloodGroupMaster.objects.get(name = form['blood_group'])
		# country_Objects = CountryMaster.objects.get(name = form['country'])
		# state_Objects = StateMaster.objects.get(name = form['state'])
		# city_Objects = CityMaster.objects.get(name = form['city'])

		user.first_name = form['first_name']
		user.last_name = form['last_name']
		profileObjects.middle_name = form['middle_name']

		user.email = form['email']
		profileObjects.email = form['email']
		profileObjects.mobile_number = form['mobile_number']
		profileObjects.gender = genderObjects
		profileObjects.blood_group = blood_Objects
		profileObjects.country = countryObjects
		profileObjects.state = stateObjects
		profileObjects.city = cityObjects
		profileObjects.date_of_birth = form['dob']
		profileObjects.address = form['address']
		profileObjects.pincode = form['pincode']
		profileObjects.aadhar_no = form['adhar_number']

		user.save()
		profileObjects.save()
		return redirect('/profile/')
	else:
		return redirect('/profile/')

def sendmessage(request):
	response = {}
	if request.method == 'POST':
		form = request.POST

		first_name = form['name']
		email = form['email']
		subject = form['subject']
		message = form['message']

		user = User.objects.get(
			first_name = first_name,
			# last_name = last_name,
			email = email,
			)

		newMessage = SendMessage.objects.get_or_create(
			name = first_name,
			email = email,
			subject = subject,
			message = message,
			)
		return render(request,'dashboard.html')
	else:
		return redirect('/contact.html/')

def upload_file(request):
	return render(request,'upload_file.html')

	




























def randomWithNDigits(n):
	range_start = 10**(n-1)
	range_end = (10**n)-1
	return randint(range_start, range_end)
