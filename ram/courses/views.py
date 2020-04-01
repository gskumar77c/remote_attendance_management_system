from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.contrib import messages
from profiles.constants.constants import constants
from . import models
from profiles import models as profile_models
from datetime import date
import datetime
# Create your views here.

def configure_base(arg,name,qtype):
	data=constants.home_page_loggedout
	if arg=='courses':
		data["title"]="courses"
		if name == "logged_in":
			if qtype == 'student':
				data["navbar"]=[["Dashboard","../profiles/dashboard"],["Enrolled Courses","../courses/enrolled_courses"],["Floated Courses","../courses/floated_courses"],["Logout","../profiles/logout"]]
			else:
				data["navbar"]=[["Dashboard","../profiles/dashboard"],["Joined Courses","../courses/joined_courses"],["Floated Courses","../courses/floated_courses"],["Logout","../profiles/logout"]]
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

	data = configure_base('courses','logged_in',qtype)

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
	data = configure_base('courses','logged_in',qtype)
	details = models.course.objects.get(course_id = courseid)
	data['details'] = details
	return render(request,'coursedetails.html',data)


def show_floated_courses(request):
	if "username" not in request.session:
		return redirect('../profiles/login')
	username=request.session["username"]
	qtype=request.session["qualification"]

	if request.method == 'POST':
		course_list = request.POST.getlist('course')
		message_string = ""
		if qtype == 'student':
			for courseid in course_list:
				course = models.course.objects.get(course_id=courseid)
				date1 = date.today()
				name = profile_models.student.objects.get(user__email = username)
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
		elif qtype == 'ta':
			for courseid in course_list:
				course = models.course.objects.get(course_id=courseid)
				date1 = date.today()
				name = profile_models.ta.objects.get(user__email = username)
				action = 'joined'
				try:
					q = models.course_ta_log.objects.filter(course=course,name=name)
					if q.__len__()==0:
						reqcourse = models.course_ta_log(course = course,date = date1,name = name,action=action)
						reqcourse.save()
					else :
						message_string = message_string + f"already joined in {course.course_id} , \n"
				except Exception as e:
						message_string = message_string + f" error in joining {course.course_id} course, \n"
			messages.warning(request,message_string)
		else:
			for courseid in course_list:
				course = models.course.objects.get(course_id=courseid)
				date1 = date.today()
				name = profile_models.instructor.objects.get(user__email = username)
				action = 'joined'
				try:
					q = models.course_instructor_log.objects.filter(course=course,name=name)
					if q.__len__()==0:
						reqcourse = models.course_instructor_log(course = course,date = date1,name = name,action=action)
						reqcourse.save()
					else :
						message_string = message_string + f"already joined in {course.course_id} , \n"
				except Exception as e:
						message_string = message_string + f" error in joining {course.course_id} course, \n"
			messages.warning(request,message_string)


	data = configure_base('courses','logged_in',qtype)
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
		if qtype == 'student':
			for courseid in course_list:
				course = models.course.objects.get(course_id=courseid)
				date1 = date.today()
				name = profile_models.student.objects.get(user__email = username)
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
		elif qtype == 'ta':
			for courseid in course_list:
				course = models.course.objects.get(course_id=courseid)
				date1 = date.today()
				name = profile_models.ta.objects.get(user__email = username)
				action = 'joined'
				try:
					q = models.course_ta_log.objects.filter(course=course,name=name)
					if q.__len__()==0:
						reqcourse = models.course_ta_log(course = course,date = date1,name = name,action=action)
						reqcourse.save()
					else :
						message_string = message_string + f"already joined in {course.course_id} , \n"
				except Exception as e:
						message_string = message_string + f" error in joining {course.course_id} course, \n"
			messages.warning(request,message_string)
		else:
			for courseid in course_list:
				course = models.course.objects.get(course_id=courseid)
				date1 = date.today()
				name = profile_models.instructor.objects.get(user__email = username)
				action = 'joined'
				try:
					q = models.course_instructor_log.objects.filter(course=course,name=name)
					if q.__len__()==0:
						reqcourse = models.course_instructor_log(course = course,date = date1,name = name,action=action)
						reqcourse.save()
					else :
						message_string = message_string + f"already joined in {course.course_id} , \n"
				except Exception as e:
						message_string = message_string + f" error in joining {course.course_id} course, \n"
			messages.warning(request,message_string)

	return redirect('floated-courses')


def enrolled_courses(request):
	if "username" not in request.session:
		return redirect('../profiles/login')
	username=request.session["username"]
	qtype=request.session["qualification"]


	data = configure_base('courses','logged_in',qtype)
	data['qtype'] = qtype
	enrolled_courses = models.course_student_log.objects.filter(name__user__email = username,action='enrolled')
	pending_courses = models.course_student_log.objects.filter(name__user__email=username,action='requested')
	completed_courses = models.course_student_log.objects.filter(name__user__email=username,action='completed')
	failed_courses = models.course_student_log.objects.filter(name__user__email=username,action='failed')
	data['completed_courses'] = list(completed_courses)
	data['failed_courses'] = list(failed_courses)
	data['pending_courses'] = list(pending_courses)
	data['enrolled_courses'] = list(enrolled_courses)
	return render(request,'enrolled_courses.html',data)


def joined_courses(request):
	if "username" not in request.session:
		return redirect('../profiles/login')
	username=request.session["username"]
	qtype=request.session["qualification"]

	data = configure_base('courses','logged_in',qtype)
	data['qtype'] = qtype
	if qtype == 'instructor' :
		joined_courses = models.course_instructor_log.objects.filter(name__user__email = username,action='joined')
		left_courses = models.course_instructor_log.objects.filter(name__user__email=username,action='left')
	else :
		joined_courses = models.course_ta_log.objects.filter(name__user__email = username,action='joined')
		left_courses = models.course_ta_log.objects.filter(name__user__email=username,action='left')
	data['joined_courses'] = list(joined_courses)
	data['left_courses'] = list(left_courses)
	return render(request,'joined_courses.html',data)


def student_requests(request):
	if "username" not in request.session:
		return redirect('../profiles/login')
	username=request.session["username"]
	qtype=request.session["qualification"]

	if request.method == 'POST':
		courseid = request.POST.get('courseid')
		list_type = request.POST.get('list_type')
		selected_students = request.POST.getlist('student')
		message_string = ""
		for student in selected_students:
				try:
					q = models.course_student_log.objects.filter(course__course_id=courseid,name__user__email=student)
					if q.__len__() != 0:
						print(q)
						for ele in q:
							ele.action = 'enrolled'
							ele.save()
					else :
						message_string = message_string + f"{student} already enrolled,\n"
				except Exception as e:
						message_string = message_string + f" error in enrolling {student}, \n"
		messages.warning(request,message_string)


	else :
		courseid = request.GET.get('id')
		list_type = request.GET.get('list_type') 

	data = configure_base('courses','logged_in',qtype)
	data['courseid'] = courseid
	data['qtype'] = qtype
	data['list_type'] = list_type
	if list_type == 'requests':
		student_list = models.course_student_log.objects.filter(course__course_id = courseid,action='requested')
	elif list_type == 'enrolled':
		student_list = models.course_student_log.objects.filter(course__course_id=courseid,action='enrolled')
	else:
		student_list = models.course_student_log.objects.filter(course__course_id=courseid,action='enrolled')
	data['student_list'] = student_list
	return render(request,'students_list.html',data)


