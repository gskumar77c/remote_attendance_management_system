from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required



@login_required
def admin_home(request):
	if request.user.is_gsadmin():
		return render(request,'users/admin_home.html')
	else :
		return redirect('auth-interface')

@login_required
def faculty_home(request):
	if request.user.is_faculty():
		return render(request,'users/faculty_home.html')
	else :
		return redirect('auth-interface')

@login_required
def student_home(request):
	if request.user.is_student():
		return render(request,'users/student_home.html')
	else :
		return redirect('auth-interface')

@login_required
def AuthenticationInterface(request):
	user = request.user
	if user.is_gsadmin():
		return redirect('admin-home')
	elif user.is_faculty():
		return redirect('faculty-home')
	else :
		return redirect('student-home')