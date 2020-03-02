from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{'course_no' : 'cs77cc$$',
	 'date_posted' : '26 feb',
	 'title' : 'software engineering',
	 'instructor' : 'sodhi'},
	 {'course_no' : 'cs304',
	 'date_posted' : '27 feb',
	 'title' : 'Computer networks',
	 'instructor' : 'raavan Demon king'},
	 {'course_no' : 'cs306',
	 'date_posted' : '77 feb',
	 'title' : 'Theory of computation',
	 'instructor' : 'soumitra'}

]

def courses(request):
	context = {'posts' : posts}
	return render(request,'RAM/courses.html',context)