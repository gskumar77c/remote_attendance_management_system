from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import attendance_register_form 
from .page_config import configure_base
from .models import attendance_register
from profiles.models import student as student_model
from profiles.models import instructor as instructor_model
from profiles.models import ta as ta_model
from datetime import datetime
# Create your views here.

def verify_authority(data):
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
            if not verify_authority(data):
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
            messages.success(request,f"sent files for marking attendance")
            return redirect('.')
            
            


    
