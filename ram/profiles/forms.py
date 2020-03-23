from django import forms
# from django.contrib.auth.forms import UserCreationForm

from .models import user
from django.contrib.auth.hashers import make_password


class register_form(forms.ModelForm):

    class Meta:
        model = user
        # fields = '__all__'
        fields=('email','full_name','dob','image','password')
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'password':forms.PasswordInput(),
            'email':forms.EmailInput()
        }

class login_form(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput,max_length=100)
    
