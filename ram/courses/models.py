from django.db import models
from institution.models import departements,period_slots
from profiles.models import instructor,ta,students


course_statuses=[('floating','floating'),('closed','closed')]

student_course_statuses=[("requested","requested"),("enrolled","enrolled"),("completed","completed"),("failed","failed")]

class course(models.Model):
    name=models.CharField(verbose_name="course name",max_length=30,unique=True,null=False)
    course_id=models.CharField(verbose_name="course id", max_length=5,unique=True,null=False)
    department=models.ForeignKey(departements,on_delete=models.CASCADE)
    pre_requisites=models.ManyToManyField("self",blank=True)
    status=models.CharField(verbose_name="status",max_length=20,choices=course_statuses)
    def __str__(self):
        return self.course_id + "    -    " + self.name

class course_student_log(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    date=models.DateField(verbose_name="date")
    name=models.ForeignKey(students,on_delete=models.CASCADE)
    action=models.CharField(max_length=10,choices=student_course_statuses)
    def __str__(self):
        return self.name.id.email + "  -  " + self.course.course_id + "   -   " + self.action

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
    date=models.DateField(verbose_name="attendance date",null=False)
    slot=models.ForeignKey(period_slots,on_delete=models.CASCADE)
    entry_timestamp=models.DateTimeField(verbose_name="timestamp of entry")
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    roll_calls=models.ManyToManyField(students)
    image=models.ImageField(verbose_name="image")
    is_extra=models.BooleanField(verbose_name="extra class",default=False)


class time_table(models.Model):
    slot=models.ForeignKey(period_slots,on_delete=models.CASCADE)
    courses=models.ManyToManyField(course)
