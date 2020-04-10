from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import attendance_register_form 
from .page_config import configure_base
from .models import attendance_register,api_queue
from profiles.models import student as student_model
from profiles.models import instructor as instructor_model
from profiles.models import ta as ta_model
from datetime import datetime
from courses.models import *
from django.utils import timezone
from django.urls import reverse
# from courses.models import course
# Create your views here.

def get_instance(username,qtype):
    if qtype=="ta":
        obj=ta_model.objects.get(user__email=username)
    elif qtype=="instructor":
        obj=instructor_model.objects.get(user__email=username)
    return obj


def verify_authority(data,username,qtype):
    ccourse=data["course"]
    # print(course.objects.all(),")"*10,type(ccourse))
    # cinst=course.objects.get(pk=ccourse)
    cdept=getattr(ccourse,"department")
    uinst=get_instance(username,qtype)
    udept=getattr(uinst,"department")

    print(cdept,udept)
    if cdept != udept:
        return False
    
    

    return True


def home(request):
    if "username" not in request.session:
        return redirect(reverse("profiles.login"))

    username=request.session["username"]
    qtype=request.session["qualification"]

    if qtype=="student":
        # messages.success(request,f"no privilage for this action")
        # return redirect('../profiles/dashboard')

        ''' display his courses and attendance for release 2'''


    data=configure_base("home",username)
    return render(request,"attendance_home.html",data)


def web_input(request):
    if "username" not in request.session:
        return redirect(reverse("profiles.login"))

    username=request.session["username"]
    qtype=request.session["qualification"]

    if qtype=="student":
        messages.success(request,f"no privilage for this action")
        return redirect(reverse("profiles.dashboard"))

    if request.method=="GET":

        form=attendance_register_form()
        data=configure_base("new attendance",username,{"form":form})
        return render(request,'new_attendance.html',data)

    else:
        form=attendance_register_form(request.POST,request.FILES)
        if form.is_valid():
            data=form.cleaned_data
            verbose_name=attendance_register.generate_attendance_verobose(data)
            if not verify_authority(data,username,qtype):
                messages.success(request,f"no privilage for this action")
                return redirect(reverse("attendance.home"))
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
            # course=form.course
            api_queue.objects.create(details=form,status="pending")
            messages.success(request,f"sent files for marking attendance")
            return redirect(reverse("attendance.details",args=(form.pk,) ))

def history_courses(request):
    
    if "username" not in request.session:
        return redirect(reverse("profiles.login"))

    username=request.session["username"]
    qtype=request.session["qualification"]

    if qtype=="student":
        messages.success(request,f"no privilage for this action")
        return redirect(reverse("profiles.dashboard"))

    ulog=None
    if qtype=="instructor":
        ulog=course_instructor_log
    if qtype=="ta":
        ulog=course_ta_log
    
    # courses=list(ulog.get_current("floating"))
    courses=list(ulog.objects.filter(name__user__email=username).order_by('action'))
    data=configure_base("history_courses",name=username,additional_dictionary={"courses":courses})
    return render(request,"history_courses.html",data)
    

def history(request,pk):

    if "username" not in request.session:
        return redirect(reverse("profiles.login"))

    username=request.session["username"]
    qtype=request.session["qualification"]

    if qtype=="student":
        messages.success(request,f"no privilage for this action")
        return redirect(reverse("attendance.home"))

    results=attendance_register.history(pk)
    data=configure_base("history_list",username,{"entries":results})
    return render(request,"history_list.html",data)

def details(request,pk):
    if "username" not in request.session:
        return redirect(reverse("profiles.login"))

    username=request.session["username"]
    qtype=request.session["qualification"]

    if qtype=="student":
        messages.success(request,f"no privilage for this action")
        return redirect(reverse("attendance.home"))


    result,names=attendance_register.details(id=pk)
    print(result.roll_calls)
    data=configure_base("details",username,{"details":result,"names":names})
    return render(request,'entry_details.html',data)

def modify(request,pk):
    if "username" not in request.session:
        return redirect(reverse("profiles.login"))

    username=request.session["username"]
    qtype=request.session["qualification"]

    if qtype=="student":
        messages.success(request,f"no privilage for this action")
        return redirect(reverse("attendance.home"))
    