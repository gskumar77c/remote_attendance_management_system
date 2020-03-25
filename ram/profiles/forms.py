from django import forms
# from django.contrib.auth.forms import UserCreationForm

from .models import user,students,instructor,ta
from django.contrib.auth.hashers import make_password


class register_form(forms.ModelForm):

    class Meta:
        model = user
        # fields = '__all__'
        fields=('email','full_name','dob','image','password','qualification')
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'password':forms.PasswordInput(),
            'email':forms.EmailInput(),
            'qualification':forms.ChoiceField()
        }

class login_form(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput,max_length=100)
    
class student_registration(forms.ModelForm):
    class Meta:
        model=students
        fields='__all__'

class instructor_registration(forms.ModelForm):
    class Meta:
        model=students
        fields='__all__'


class ta_registration(forms.ModelForm):
    class Meta:
        model=students
        fields='__all__'

