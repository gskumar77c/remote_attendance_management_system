from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class StudentRegistrationForm(forms.Form):
	branch_options = (
						('CSE','computer-science'),
						('EEE','electrical'),
						('CHE','chemical'),
						('MEB','mechanical'),
						('CEB','civil')
						)
	email  = forms.CharField(max_length=250,widget = forms.EmailInput(attrs={"class":"form-control","placeholder":"Email *"}))
	password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password *"}))
	fullname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Full Name *"}))
	branch  = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control","placeholder":"Email *"}),choices= branch_options)



class FacultyRegistrationForm(forms.Form):
	branch_options = (
						('CSE','computer-science-department'),
						('EEE','electrical-department'),
						('CHE','chemical-department'),
						('MEB','mechanical-department'),
						('CEB','civil-department')
						)
	email  = forms.CharField(max_length=250,widget = forms.EmailInput(attrs={"class":"form-control","placeholder":"Email *"}))
	password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password *"}))
	fullname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Full Name *"}))
	department  = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}),choices= branch_options)


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        if user.admin :
            user.student = False
            user.gsadmin=True
        user.save()
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        return self.initial["password"]