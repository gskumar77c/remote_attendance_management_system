from django.db import models
from institution.models import departements,days
from profiles.models import instructor
from profiles.models import students
# Create your models here.

course_statuses=[('floating','floating'),('open','open'),('closed','closed')]

class courses(models.Model):
    name=models.CharField(name="course name",max_length=20,unique=True,null=False)
    id=models.CharField(name="course id", max_length=5,unique=True,null=False)
    department=models.ForeignKey(departements)
    instructors=models.ManyToManyField(instructor)
    students=models.ManyToManyField(students)
    pre_requisites=models.ManyToManyField(courses)
    status=models.CharField(name="status",max_length=20,choices=course_statuses)

class attendance(models.Model):
    date=models.DateField(name="attendance date",null=False)
    day=models.CharField(name="date",choices=days)
    slot=models.IntegerChoices(name="slot number",choices=[1,2,3,4,5,6,7])
    entry_timestamp=models.DateTimeField(name="timestamp of entry")
    course=models.ForeignKey(courses)
    is_extra=models.BooleanField(name="extra class",default=False)
    roll_calls=models.ManyToManyField(students)
    image=models.ImageField(name="image")
    