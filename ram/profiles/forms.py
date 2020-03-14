from django import forms
# from django.contrib.auth.forms import UserCreationForm

from .models import user
from django.contrib.auth.hashers import make_password


class register_form(forms.ModelForm):
    # test=forms.CharField()
    class Meta:
        model = user
        fields = '__all__'
        # fields=('email','dob')
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'password':forms.PasswordInput()
        }
    # def clean(self):
    #     cleaned_data = super(register_form, self).clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")

    #     if password != conf irm_password:
    #         raise forms.ValidationError(
    #             "password and confirm_password does not match"
    #         )
    # def save(self):
    #     # return 
    #     # print(self["username"])
    #     # print(self)
    #     # self._mutable = True
    #     # new=make_password(self.cleaned_data['password'])
    #     # self['password']=new
    #     # self._mutable=False
    #     # print(">>",self.cleaned_data)
    #     # # request.POST["password"]=new
    #     # print("\n***8 check here \n",self)
    #     return super().save()

class login_form(forms.Form):
    email=forms.EmailField()
    password=forms.PasswordInput()
