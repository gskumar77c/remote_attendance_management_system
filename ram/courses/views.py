from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.contrib import messages
from profiles.constants.constants import constants
from . import models
from profiles.models import student,instructor,ta,user
from datetime import date
import datetime
from .page_config import configure_base
# Create your views here.
from django.urls import reverse


def all_courses(request):
	if "username" not in request.session:
		return redirect(reverse("profiles.login"))
	username=request.session["username"]
	qtype=request.session["qualification"]


	data = configure_base('courses',username,{'qtype':qtype})

	# list of all courses
	courses = models.course.objects.all().order_by('department')
	data['courses'] = list(courses)
	return render(request,'courses.html',data)
    

def coursedetails(request):
	if "username" not in request.session:
		return  redirect(reverse("profiles.login"))

	username=request.session["username"]
	qtype=request.session["qualification"]

	courseid = request.GET.get('id')
	data = configure_base('course-details',username,{'qtype':qtype})
	details = models.course.objects.get(course_id = courseid)
	data['details'] = details
	return render(request,'coursedetails.html',data)


def show_floated_courses(request):
	if "username" not in request.session:
		return  redirect(reverse("profiles.login"))

	username=request.session["username"]
	qtype=request.session["qualification"]
	usr = user.objects.get(email=username)
	if usr.status == False:
		return  redirect(reverse("courses.all"))
	

	if request.method == 'POST':
		course_list = request.POST.getlist('course')
		message_string = ""
		if qtype == 'student':
			for courseid in course_list:
				course = models.course.objects.get(course_id=courseid)
				date1 = date.today()
				name = student.objects.get(user__email = username)
				action = 'requested'
				try:
					q = models.course_student_log.current_status()
					q = q.filter(course=course,name=name)
					#q = models.course_student_log.objects.filter(course=course,name=name)
					if q.__len__()==0:
						reqcourse = models.course_student_log(course = course,timestamp = date1,name = name,action=action)
						reqcourse.save()
					else :
						for ele in q:
							message_string = message_string + f"request denied as {course.course_id} is in {ele.action} state, \n"
				except Exception as e:
						message_string = message_string + f" error in adding {course.course_id} course, \n"
			messages.warning(request,message_string)	
		elif qtype == 'ta':
			for courseid in course_list:
				course = models.course.objects.get(course_id=courseid)
				date1 = date.today()
				name = ta.objects.get(user__email = username)
				action = 'joined'
				try:
					q = models.course_ta_log.current_status()
					q = q.filter(course=course,name=name)
					#q = models.course_ta_log.objects.filter(course=course,name=name)
					if q.__len__()==0:
						reqcourse = models.course_ta_log(course = course,timestamp = date1,name = name,action=action)
						reqcourse.save()
					else :
						for ele in q:
							message_string = message_string + f"already {ele.action}  in {course.course_id} , \n"
				except Exception as e:
						message_string = message_string + f" error in joining {course.course_id} course, \n"
			messages.warning(request,message_string)
		else:
			for courseid in course_list:
				course = models.course.objects.get(course_id=courseid)
				date1 = date.today()
				name = instructor.objects.get(user__email = username)
				action = 'joined'
				try:
					q = models.course_instructor_log.current_status()
					q = q.filter(course=course,name=name)
					#q = models.course_instructor_log.objects.filter(course=course,name=name)
					if q.__len__()==0:
						reqcourse = models.course_instructor_log(course = course,timestamp = date1,name = name,action=action)
						reqcourse.save()
					else :
						for ele in q:
							message_string = message_string + f"already {ele.action} in {course.course_id} , \n"
				except Exception as e:
						message_string = message_string + f" error in joining {course.course_id} course, \n"
			messages.warning(request,message_string)

	data = configure_base('floated-courses',username,{'qtype':qtype})
	if qtype == 'student':
		floated_courses = models.course.objects.filter(status='floating').order_by('department')
	else :
		floated_courses = models.course.objects.filter().order_by('department')
	data['courses'] = list(floated_courses)
	return render(request,'floatedcourses.html',data)



def enrolled_courses(request):
	if "username" not in request.session:
		return  redirect(reverse("profiles.login"))

	username=request.session["username"]
	qtype=request.session["qualification"]
	usr = user.objects.get(email=username)
	if usr.status == False:
		return  redirect(reverse("courses.all"))

	


	if request.method == 'POST':
		course_list = request.POST.getlist('course')
		message_string = ""
		if qtype == 'student':
			for courseid in course_list:
				course = models.course.objects.get(course_id=courseid)
				date1 = date.today()
				name = student.objects.get(user__email = username)
				action='enrolled'
				try:
					q = models.course_student_log.get_current(action)
					q = q.filter(course=course,name=name)
					#q = models.course_student_log.objects.filter(course=course,name=name,action=action)
					if q.__len__() != 0:
						for ele in q:
							dropcourse = models.course_student_log(course = ele.course,timestamp = date1,name = ele.name,action='dropped')
							dropcourse.save()
					else :
						message_string = message_string + f" {course.course_id} already dropped, \n"
				except Exception as e:
						message_string = message_string + f" error in dropping {course.course_id} course, \n"
			messages.warning(request,message_string)


	data = configure_base('enrolled-courses',username,{'qtype':qtype})
	current_list = models.course_student_log.current_status()
	enrolled_courses = current_list.filter(name__user__email = username,action='enrolled')
	pending_courses = current_list.filter(name__user__email=username,action='requested')
	completed_courses = current_list.filter(name__user__email=username,action='completed')
	failed_courses = current_list.filter(name__user__email=username,action='failed')
	data['completed_courses'] = list(completed_courses)
	data['failed_courses'] = list(failed_courses)
	data['pending_courses'] = list(pending_courses)
	data['enrolled_courses'] = list(enrolled_courses)
	return render(request,'enrolled_courses.html',data)


def joined_courses(request):
	if "username" not in request.session:
		return  redirect(reverse("profiles.login"))

	username=request.session["username"]
	qtype=request.session["qualification"]
	usr = user.objects.get(email=username)
	if usr.status == False:
		return redirect(reverse("courses.all"))


	data = configure_base('joined-courses',username,{'qtype':qtype})
	if qtype == 'instructor' :
		joined_courses = models.course_instructor_log.current_status().filter(name__user__email = username,action='joined')
		left_courses = models.course_instructor_log.current_status().filter(name__user__email=username,action='left')
	else :
		joined_courses = models.course_ta_log.current_status().filter(name__user__email = username,action='joined')
		left_courses = models.course_ta_log.current_status().filter(name__user__email=username,action='left')
	data['joined_courses'] = list(joined_courses)
	data['left_courses'] = list(left_courses)
	return render(request,'joined_courses.html',data)


def student_requests(request):
	if "username" not in request.session:
		return  redirect(reverse("profiles.login"))
	username=request.session["username"]
	qtype=request.session["qualification"]
	usr = user.objects.get(email=username)
	if usr.status == False:
		return redirect(reverse("courses.all"))


	if request.method == 'POST':
		courseid = request.POST.get('courseid')
		list_type = request.POST.get('list_type')
		selected_students = request.POST.getlist('student')
		message_string = ""
		date1 = date.today()
		for student in selected_students:
				try:
					q = models.course_student_log.current_status().filter(course__course_id=courseid,name__user__email=student,action='requested')
					if q.__len__() != 0:
						for ele in q:
							enrollcourse = models.course_student_log(course = ele.course,timestamp = date1,name = ele.name,action='enrolled')
							enrollcourse.save()
					else :
						message_string = message_string + f"{student} request is invalid,\n"
				except Exception as e:
						message_string = message_string + f" error in enrolling {student}, \n"
		messages.warning(request,message_string)


	else :
		courseid = request.GET.get('id')
		list_type = request.GET.get('list_type') 


	fields = {}
	fields['qtype'] = qtype
	fields['courseid'] = courseid
	fields['list_type'] = list_type
	data = configure_base('student-requests',username,fields)

	if list_type == 'requests':
		student_list = models.course_student_log.current_status().filter(course__course_id = courseid,action='requested')
	elif list_type == 'enrolled':
		student_list = models.course_student_log.current_status().filter(course__course_id=courseid,action='enrolled')
	else:
		student_list = models.course_student_log.current_status().filter(course__course_id=courseid,action='enrolled')
	data['student_list'] = student_list
	return render(request,'students_list.html',data)


