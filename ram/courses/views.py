from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.contrib import messages
from profiles.constants.constants import constants
from . import models
from profiles import models as profile_models
from datetime import date
# Create your views here.

def configure_base(arg,name):
    data=constants.home_page_loggedout
    if arg=='courses':        
        data["title"]="courses"
        if name == "logged_in":
            data["navbar"]=[["Dashboard","../profiles/dashboard"],["Enrolled Courses","../courses/enrolled_courses"],["Floated Courses","../courses/floated_courses"],["Logout","../profiles/logout"]]
            data["type"]="Logout"
            data["type_link"]="../profiles/logout"
            data["name"]=name
            data["form"]={}
        else:
            data["navbar"]=[["Login","../profiles/login"]]
            data["type"]="Login"
            data["type_link"]="../profiles/login"
            data["name"]=name
            data["form"]={}
        
        return data


def all_courses(request):
	if "username" not in request.session:
		return redirect('../profiles/login')
	username=request.session["username"]
	qtype=request.session["qualification"]

	# #for testing and implementing
	# username = 'a@gmail.com'
	# qtype = 'student'

	data = configure_base('courses','logged_in')

	# list of all courses
	courses = models.course.objects.all().order_by('department')
	data['courses'] = list(courses)
	data['qtype'] = qtype
	return render(request,'courses.html',data)
    

def coursedetails(request):
	if "username" not in request.session:
		return redirect('../profiles/login')
	username=request.session["username"]
	qtype=request.session["qualification"]

	courseid = request.GET.get('id')
	data = configure_base('courses','logged_in')
	details = models.course.objects.get(course_id = courseid)
	data['details'] = details
	return render(request,'coursedetails.html',data)


def show_floated_courses(request):
	if "username" not in request.session:
		return redirect('../profiles/login')
	username=request.session["username"]
	qtype=request.session["qualification"]

	data = configure_base('courses','logged_in')
	floated_courses = models.course.objects.filter(status='floating').order_by('department')
	data['courses'] = list(floated_courses)
	data['qtype'] = qtype
	return render(request,'floatedcourses.html',data)


def send_request(request):
	if "username" not in request.session:
		return redirect('../profiles/login')
	username=request.session["username"]
	qtype=request.session["qualification"]


	if request.method == 'POST':
		course_list = request.POST.getlist('course')
		message_string = ""
		for courseid in course_list:
			course = models.course.objects.get(course_id=courseid)
			date1 = date.today()
			name = profile_models.students.objects.get(id__email = username)
			action = 'requested'
			try:
				q = models.course_student_log.objects.filter(course=course,name=name)
				if q.__len__()==0:
					reqcourse = models.course_student_log(course = course,date = date1,name = name,action=action)
					reqcourse.save()
				else :
					message_string = message_string + f" {course.course_id} already in pending, \n"
			except Exception as e:
					message_string = message_string + f" error in adding {course.course_id} course, \n"
		messages.warning(request,message_string)	

	return redirect('floated-courses')


def enrolled_courses(request):
	if "username" not in request.session:
		return redirect('../profiles/login')
	username=request.session["username"]
	qtype=request.session["qualification"]


	data = configure_base('courses','logged_in')
	data['qtype'] = qtype
	enrolled_courses = models.course_student_log.objects.filter(name__id__email = username,action='enrolled')
	pending_courses = models.course_student_log.objects.filter(name__id__email=username,action='requested')
	completed_courses = models.course_student_log.objects.filter(name__id__email=username,action='completed')
	failed_courses = models.course_student_log.objects.filter(name__id__email=username,action='failed')
	data['completed_courses'] = list(completed_courses)
	data['failed_courses'] = list(failed_courses)
	data['pending_courses'] = list(pending_courses)
	data['enrolled_courses'] = list(enrolled_courses)
	return render(request,'enrolled_courses.html',data)
