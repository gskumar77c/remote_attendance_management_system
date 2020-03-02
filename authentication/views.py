from django.shortcuts import render,redirect
from .forms import FacultyRegistrationForm,StudentRegistrationForm
from .models import StudentRequests,FacultyRequests,User
from django import forms
from django.contrib import messages


def register(request):
	form1 = StudentRegistrationForm()
	form2 = FacultyRegistrationForm()
	return render(request,'authentication/register.html',{'student_form':form1,'faculty_form':form2})

def student_register(request):
	if request.method == 'POST':
		form = StudentRegistrationForm(request.POST)
		if form.is_valid():
			usr = form.cleaned_data.get('email')
			passwd = form.cleaned_data.get('password')
			fullname = form.cleaned_data.get('fullname')
			branch = form.cleaned_data.get('branch')
			qs = StudentRequests.objects.filter(email = usr)
			gs = User.objects.filter(email=usr)
			fs = FacultyRequests.objects.filter(email=usr)
			if gs.exists():
				messages.warning(request, 'You already have an account with this email')
			elif qs.exists():
				messages.warning(request,"You have already requested with this email")
			elif fs.exists():
				messages.warning(request,"Already have a request for Faculty account creation with this email")
			else :
				std = StudentRequests(email = usr,password = passwd,fullname=fullname,branch=branch)
				std.save()
				messages.success(request,'Request for account creation has been sent to admin')
				return redirect('login')
	return redirect('gsregister')


def faculty_register(request):
	if request.method == 'POST':
		form = FacultyRegistrationForm(request.POST)
		if form.is_valid():
			usr = form.cleaned_data.get('email')
			passwd = form.cleaned_data.get('password')
			fullname = form.cleaned_data.get('fullname')
			department = form.cleaned_data.get('department')
			qs = FacultyRequests.objects.filter(email = usr)
			gs = User.objects.filter(email=usr)
			ss = StudentRequests.objects.filter(email=usr)
			if gs.exists():
				messages.warning(request, 'You already have an account with this email')
			elif qs.exists():
				messages.warning(request,"You have already requested with this email")
			elif ss.exists():
				messages.warning(request,"Already have a request for Student account creation with this email")
			else :
				std = FacultyRequests(email = usr,password = passwd,fullname=fullname,department=department)
				std.save()
				messages.success(request,'Request for account creation has been sent to admin')
				return redirect('login')
	return redirect('gsregister')

'''
def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']

		print(email,password)
	return render(request,'authentication/login.html')
'''