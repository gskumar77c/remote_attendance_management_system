from django import forms
# from django.contrib.auth.forms import UserCreationForm

# from .models import user,student,instructor,ta

from .models import user as user_model
from .models import student as student_model
from .models import instructor as instructor_model
from .models import ta as ta_model

from django.contrib.auth.hashers import make_password


class register_form(forms.ModelForm):

    def clean_password(self):
        name = self.cleaned_data['password']
        hashed_password=make_password(self.cleaned_data['password'])
        return hashed_password

    prefix="user"

    class Meta:
        model = user_model
        # fields = '__all__'
        fields=('email','full_name','dob','image','password','qualification')
        ## change
        # fields=('id','full_name','dob','image','password','qualification')
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'password':forms.PasswordInput(),
            'id':forms.EmailInput(),
            # 'qualification':forms.ChoiceField()
        }

class login_form(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput,max_length=100)
    
class student_registration(forms.ModelForm):
    prefix="student"
    class Meta:
        model=student_model
        # fields='__all__'
        fields=('semester',)
        # exclude=['email']

class instructor_registration(forms.ModelForm):
    prefix="instructor"
    class Meta:
        model=instructor_model
        fields=('department',)
        # exclude=['email']



class ta_registration(forms.ModelForm):
    prefix="ta"
    class Meta:
        model=ta_model
        fields=('department',)
        # exclude=['email']
