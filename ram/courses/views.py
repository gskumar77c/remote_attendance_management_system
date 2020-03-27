from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.contrib import messages
from institution.views import configure_base
from . import models

# Create your views here.
def all_courses(request):
	# we'll add this at last
	# if "username" not in request.session:
	# 	return redirect('../profiles/login')
	# username=request.session["username"]
	# qtype=request.session["qualification"]

	#for testing and implementing
	username = 'a@gmail.com'
	qtype = 'student'
	courses = models.course.objects.all()
	data = configure_base('home','Not logged in')
	data['courses'] = list(courses)
	return render(request,'courses.html',data)
    