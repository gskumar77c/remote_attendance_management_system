from django.db import models
from institution.models import departements,period_slots
from profiles.models import instructor,ta,students


course_statuses=[('floating','floating'),('closed','closed')]

student_course_statuses=[("requested","requested"),("enrolled","enrolled"),("completed","completed"),("failed","failed")]

class course(models.Model):
    name=models.CharField(verbose_name="course name",max_length=20,unique=True,null=False)
    id=models.CharField(verbose_name="course id", max_length=5,unique=True,null=False)
    department=models.ForeignKey(institution_module.departements,on_delete=models.CASCADE)
    pre_requisites=models.ManyToManyField("self")
    status=models.CharField(verbose_name="status",max_length=20,choices=course_statuses)

class course_student_log(models.Model)
    course=models.ForeignKey(course)
    date=models.datetime(verbose_name="date")
    name=models.ForeignKey(students)
    action=models.CharField(max_length=10,choices=student_course_statuses)

class course_instructor_log(models.Model)
    course=models.ForeignKey(course)
    date=models.datetime(verbose_name="date")
    name=models.ForeignKey(instructor,on_delete=models.CASCADE)
    action=models.CharField(max_length=10,choices=[("joined","joined"),("left","left")])

class course_ta_log(models.Model)
    course=models.ForeignKey(course)
    date=models.datetime(verbose_name="date")
    name=models.ForeignKey(ta,on_delete=models.CASCADE)
    action=models.CharField(max_length=10,choices=[("joined","joined"),("left","left")])

class attendance(models.Model):
    date=models.DateField(verbose_name="attendance date",null=False)
    slot=models.ForeignKey(period_slots,on_delete=models.CASCADE)
    entry_timestamp=models.DateTimeField(verbose_name="timestamp of entry")
    course=models.ForeignKey(courses,on_delete=models.CASCADE)
    roll_calls=models.ManyToManyField(profiles_module.students)
    image=models.ImageField(verbose_name="image")
    is_extra=models.BooleanField(verbose_name="extra class",default=False)


class time_table(models.Model):
    slot=models.ForeignKey(period_slots,on_delete=models.CASCADE)
    courses=models.ManyToManyField(courses)
