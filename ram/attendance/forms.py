from django import forms
from .models import attendance_register as attendance_register_model

class attendance_register_form(forms.ModelForm):
    class Meta:
        model=attendance_register_model
        fields=('date','slot','is_extra','course','images')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
