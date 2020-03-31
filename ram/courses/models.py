from django.db import models
from institution.models import department as department_model
from institution.models import period_slot as period_slot_model
from profiles.models import user as user_model
from profiles.models import student as student_model
from profiles.models import instructor as instructor_model
from profiles.models import ta as ta_model

course_statuses=[('floating','floating'),('closed','closed')]

student_course_statuses=[("requested","requested"),("enrolled","enrolled"),("completed","completed"),("failed","failed")]

class course(models.Model):
    name=models.CharField(verbose_name="course name",max_length=30,unique=True,null=False)
    course_id=models.CharField(verbose_name="course id", max_length=5,unique=True,null=False,primary_key=True)
    department=models.ForeignKey(department_model,on_delete=models.CASCADE)
    pre_requisites=models.ManyToManyField("self",blank=True)
    status=models.CharField(verbose_name="status",max_length=20,choices=course_statuses)
    def __str__(self):
        return self.course_id + "    -    " + self.name

class course_student_log(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    date=models.DateField(verbose_name="date")
    name=models.ForeignKey(student_model,on_delete=models.CASCADE)
    action=models.CharField(max_length=10,choices=student_course_statuses)
    def __str__(self):
        return self.name.user.email + "  -  " + self.course.course_id + "   -   " + self.action

class course_instructor_log(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    date=models.DateField(verbose_name="date")
    name=models.ForeignKey(instructor_model,on_delete=models.CASCADE)
    action=models.CharField(max_length=10,choices=[("joined","joined"),("left","left")])
    def __str__(self):
        return self.name.user.email + "  -  " + self.course.course_id + "   -   " + self.action

class course_ta_log(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    date=models.DateField(verbose_name="date")
    name=models.ForeignKey(ta_model,on_delete=models.CASCADE)
    action=models.CharField(max_length=10,choices=[("joined","joined"),("left","left")])
    def __str__(self):
        return self.name.user.email + "  -  " + self.course.course_id + "   -   " + self.action




class time_table(models.Model):
    slot=models.ForeignKey(period_slot_model,on_delete=models.CASCADE)
    courses=models.ManyToManyField(course)
