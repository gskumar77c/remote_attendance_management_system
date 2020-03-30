from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.contrib import messages
from .models import course as course_model
from .models import course_student_log,course_instructor_log,course_ta_log
from profiles.models import user as user_model
from profiles.models import student as student_model
from profiles.models import instructor as instructor_model
from profiles.models import ta as ta_model
from .page_config import configure_base

from datetime import date
# Create your views here.




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
	courses = course_model.objects.all().order_by('department')
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
	details = course_model.objects.get(course_id = courseid)
	data['details'] = details
	return render(request,'coursedetails.html',data)


def show_floated_courses(request):
	if "username" not in request.session:
		return redirect('../profiles/login')
	username=request.session["username"]
	qtype=request.session["qualification"]

	data = configure_base('courses','logged_in')
	floated_courses = course_model.objects.filter(status='floating').order_by('department')
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
			course = course_model.objects.get(course_id=courseid)
			date1 = date.today()
			name = student_model.objects.get(user = username)
			action = 'requested'
			try:
				q = course_student_log.objects.filter(course=course,name=name)
				if q.__len__()==0:
					reqcourse = course_student_log(course = course,date = date1,name = name,action=action)
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
	enrolled_courses = course_student_log.objects.filter(name = username,action='enrolled')
	pending_courses = course_student_log.objects.filter(name=username,action='requested')
	completed_courses = course_student_log.objects.filter(name=username,action='completed')
	failed_courses = course_student_log.objects.filter(name=username,action='failed')
	data['completed_courses'] = list(completed_courses)
	data['failed_courses'] = list(failed_courses)
	data['pending_courses'] = list(pending_courses)
	data['enrolled_courses'] = list(enrolled_courses)
	return render(request,'enrolled_courses.html',data)
