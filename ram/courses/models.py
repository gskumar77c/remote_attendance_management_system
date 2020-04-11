from django.db import models
from institution.models import department as department_model
from institution.models import period_slot as period_slot_model
from profiles.models import user as user_model
from profiles.models import student as student_model
from profiles.models import instructor as instructor_model
from profiles.models import ta as ta_model

course_statuses=[('floating','floating'),('closed','closed')]

student_course_statuses=[("requested","requested"),("enrolled","enrolled"),("completed","completed"),("failed","failed"),("dropped","dropped")]

def raw_to_queryset(rawqset,model_name):
    wanted_items = set()
    for item in rawqset:
        wanted_items.add(item.pk)
    return model_name.objects.filter(pk__in = wanted_items)

class course(models.Model):
    name=models.CharField(verbose_name="course name",max_length=30,unique=True,null=False)
    course_id=models.CharField(verbose_name="course id", max_length=5,unique=True,null=False,primary_key=True)
    department=models.ForeignKey(department_model,on_delete=models.CASCADE)
    pre_requisites=models.ManyToManyField("self",blank=True)
    status=models.CharField(verbose_name="status",max_length=20,choices=course_statuses)
    
    def __str__(self):
        s=self.course_id + "," + self.name
        return s or ''
class course_student_log(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(verbose_name="Time stamp")
    name=models.ForeignKey(student_model,on_delete=models.CASCADE)
    action=models.CharField(max_length=10,choices=student_course_statuses)
    
    @classmethod
    def current_status(cls):
        results=course_student_log.objects.raw("SELECT id FROM courses_course_student_log as t1 where  t1.timestamp=(SELECT max(t2.timestamp) from courses_course_student_log as t2 where t2.name_id=t1.name_id and t2.course_id=t1.course_id )")
        results=raw_to_queryset(results,cls)
        return results

    @classmethod
    def get_current(cls,action_type):
        res=cls.current_status()
        res=res.filter(action=action_type)
        return res


    def __str__(self):
        s=self.name.user.email + "  -  " + self.course.course_id + "   -   " + self.action
        return s or ''
    

class course_instructor_log(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(verbose_name="timestamp")
    name=models.ForeignKey(instructor_model,on_delete=models.CASCADE)
    action=models.CharField(max_length=10,choices=[("joined","joined"),("left","left")])

    @classmethod
    def current_status(cls):
        results=course_student_log.objects.raw("SELECT id FROM courses_course_instructor_log as t1 where  t1.timestamp=(SELECT max(t2.timestamp) from courses_course_instructor_log as t2 where t2.name_id=t1.name_id and t2.course_id=t1.course_id )")
        results=raw_to_queryset(results,cls)
        return results

    @classmethod
    def get_current(cls,action_type):
        res=cls.current_status()
        res=res.filter(action=action_type)
        return res


    def __str__(self):
        s=self.name.user.email + "  -  " + self.course.course_id + "   -   " + self.action
        return s or ''

class course_ta_log(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(verbose_name="timestamp")
    name=models.ForeignKey(ta_model,on_delete=models.CASCADE)
    action=models.CharField(max_length=10,choices=[("joined","joined"),("left","left")])

    @classmethod
    def current_status(cls):
        results=course_student_log.objects.raw("SELECT id FROM courses_course_ta_log as t1 where  t1.timestamp=(SELECT max(t2.timestamp) from courses_course_ta_log as t2 where t2.name_id=t1.name_id and t2.course_id=t1.course_id )")
        results=raw_to_queryset(results,cls)
        return results

    @classmethod
    def get_current(cls,action_type):
        res=cls.current_status()
        res=res.filter(action=action_type)
        return res


    def __str__(self):
        s=self.name.user.email + "  -  " + self.course.course_id + "   -   " + self.action

        return s or ''



class time_table(models.Model):
    slot=models.ForeignKey(period_slot_model,on_delete=models.CASCADE)
    courses=models.ManyToManyField(course)
