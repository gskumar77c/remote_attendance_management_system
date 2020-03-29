from django.db import models
from institution.models import department,period_slot
from profiles.models import instructor,ta,student


course_statuses=[('floating','floating'),('closed','closed')]

student_course_statuses=[("requested","requested"),("enrolled","enrolled"),("completed","completed"),("failed","failed")]

class course(models.Model):
    name=models.CharField(verbose_name="course name",max_length=20,unique=True,null=False)
    course_id=models.CharField(verbose_name="course id", max_length=5,unique=True,null=False,primary_key=True)
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    pre_requisites=models.ManyToManyField("self")
    status=models.CharField(verbose_name="status",max_length=20,choices=course_statuses)

class course_student_log(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    date=models.DateField(verbose_name="date")
    name=models.ForeignKey(student,on_delete=models.CASCADE)
    action=models.CharField(max_length=10,choices=student_course_statuses)

class course_instructor_log(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    date=models.DateField(verbose_name="date")
    name=models.ForeignKey(instructor,on_delete=models.CASCADE)
    action=models.CharField(max_length=10,choices=[("joined","joined"),("left","left")])

class course_ta_log(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    date=models.DateField(verbose_name="date")
    name=models.ForeignKey(ta,on_delete=models.CASCADE)
    action=models.CharField(max_length=10,choices=[("joined","joined"),("left","left")])

class attendance(models.Model):
    attendance_verbose=models.CharField(max_length=50,primary_key=True)
    date=models.DateField(verbose_name="attendance date",null=False)
    slot=models.ForeignKey(period_slot,on_delete=models.CASCADE)
    entry_timestamp=models.DateTimeField(verbose_name="timestamp of entry")
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    roll_calls=models.ManyToManyField(student)
    image=models.ImageField(verbose_name="image")
    is_extra=models.BooleanField(verbose_name="extra class",default=False)


class time_table(models.Model):
    slot=models.ForeignKey(period_slot,on_delete=models.CASCADE)
    courses=models.ManyToManyField(course)
