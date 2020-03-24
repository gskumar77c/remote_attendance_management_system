from django.db import models
from courses.models import courses

days=[('monday','monday'),('tuesday','tuesday'),('wednesday','wednesday'),('thursday','thursday'),('friday','friday'),('saturday','saturday'),('sunday','sunday'),]
# Create your models here.
class public_announcements(models.Model):
    
    date=models.DateTimeField(name='date')
    info=models.TextField(name='info')

class departements(models.Model):
    name=models.CharField(name="department",max_length=20,unique=True,null=False)

class time_table(models.Model):
    day=models.CharField(name="day",choices=days)
    time=models.IntegerChoices(name="Slot",choices=[1,2,3,4,5,6,7])
    course=models.ManyToManyField(courses)