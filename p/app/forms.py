from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class Regis_stu_form(forms.Form):
    stu_name = forms.CharField(max_length=90)
    mobile = forms.IntegerField()
    age = forms.IntegerField()
    address = forms.CharField(max_length=90)
    course = forms.ChoiceField(choices=[("c","c"),("c++","c++")])
    fees = forms.IntegerField()
    paid_fees = forms.IntegerField()
    trainer_name = forms.CharField(max_length=20)

    # class Meta:
    #     model=Regis_stu
    #     fields='__all__'

class Enq_form(forms.ModelForm):
    class Meta:
        model=Enq
        fields='__all__'

class User_regis_form(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

