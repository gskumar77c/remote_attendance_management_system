from django.db import models
from courses.models import course as course_model
from institution.models import period_slot as period_slot_model
# from profiles.models import user as user_model
from profiles.models import student as student_model
from profiles.models import instructor as instructor_model
from profiles.models import ta as ta_model

api_results=[('success','success'),('failure','failure'),('pending','pending')]

# Create your models here.
def create_zip(instance,filename):
    filename="attendance images/"+instance.attendance_verbose+".zip"
    print("created zip file:",filename)
    return filename


class attendance_register(models.Model):
    attendance_verbose=models.CharField(max_length=100)
    date=models.DateField(verbose_name="attendance date",null=False)
    slot=models.ForeignKey(period_slot_model,on_delete=models.CASCADE)
    entry_instructor=models.ForeignKey(instructor_model,on_delete=models.CASCADE,null=True)
    entry_ta=models.ForeignKey(ta_model,on_delete=models.CASCADE,null=True)
    entry_timestamp=models.DateTimeField(verbose_name="timestamp of entry")
    course=models.ForeignKey(course_model,on_delete=models.CASCADE)
    roll_calls=models.ManyToManyField(student_model,null=True)
    images=models.FileField(verbose_name="images zip",upload_to=create_zip)
    is_extra=models.BooleanField(verbose_name="extra class",default=False)
    is_marked=models.BooleanField(verbose_name="Attendance marked by Vidmi",default=False)

    def __str__(self):
        return self.attendance_verbose

    @classmethod
    def generate_attendance_verobose(cls,data):
        # data=form.cleaned_data

        string=str(data["date"])+"."+str(data["slot"])+"."+str(data["course"])
        return string

class api_queue(models.Model):
    details=models.ForeignKey(attendance_register,on_delete=models.CASCADE)
    status=models.CharField(max_length=10,choices=api_results,default='pending')
    
