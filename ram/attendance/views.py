from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import attendance_register_form 
from .page_config import configure_base
from .models import attendance_register,api_queue
from profiles.models import student as student_model
from profiles.models import instructor as instructor_model
from profiles.models import ta as ta_model
from datetime import datetime
from courses.models import course
from django.utils import timezone
# Create your views here.

def get_instance(username,qtype):
    if qtype=="ta":
        obj=ta_model.objects.get(user__email=username)
    elif qtype=="instructor":
        obj=instructor_model.objects.get(user__email=username)
    return obj

def verify_authority(data,username,qtype):
    course=data["course"]
    cinst=course.objects.get(course_id=course)
    cdept=getattr(cinst,"department")
    uinst=get_instance(username,qtype)
    udept=getattr(uinst,"department")

    if cdept != udept:
        return False
    
    

    return True



def web_input(request):
    if "username" not in request.session:
        return redirect('../profiles/login')

    username=request.session["username"]
    qtype=request.session["qualification"]

    if qtype=="student":
        messages.success(request,f"no privilage for this action")
        return redirect('../profiles/dashboard')

    if request.method=="GET":

        form=attendance_register_form()
        data=configure_base("attendance",username,{"form":form})
        return render(request,'attendance.html',data)

    else:
        form=attendance_register_form(request.POST,request.FILES)
        if form.is_valid():
            data=form.cleaned_data
            verbose_name=attendance_register.generate_attendance_verobose(data)
            if not verify_authority(data,username):
                messages.success(request,f"no privilage for this action")
                return redirect('../home')
            form=form.save(commit=False)
            form.attendance_verbose=verbose_name
            print(form.attendance_verbose,"|"*10)
            if qtype=="ta":
                obj=ta_model.objects.get(user__email=username)
                form.entry_ta=obj
            
            else:
                obj=instructor_model.objects.get(user__email=username)
                form.entry_instructor=obj
            form.entry_timestamp=datetime.today()
            form.save()
            api_queue.objects.Create(form)
            messages.success(request,f"sent files for marking attendance")
            return redirect('.')

def history(request):

    if "username" not in request.session:
        return redirect('../profiles/login')

    username=request.session["username"]
    qtype=request.session["qualification"]

    if qtype=="student":
        messages.success(request,f"no privilage for this action")
        return redirect('../profiles/dashboard')

    results=attendance_register.history(username)

def detail(request):
    if "username" not in request.session:
        return redirect('../profiles/login')

    username=request.session["username"]
    qtype=request.session["qualification"]

    if qtype=="student":
        messages.success(request,f"no privilage for this action")
        return redirect('../profiles/dashboard')

def modify(request):
    if "username" not in request.session:
        return redirect('../profiles/login')

    username=request.session["username"]
    qtype=request.session["qualification"]

    if qtype=="student":
        messages.success(request,f"no privilage for this action")
        return redirect('../profiles/dashboard')
    