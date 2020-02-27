
from django import forms
from django.forms import ModelForm
from cvdata.models import *


class CVDataForm(forms.ModelForm):

    class Meta:
        model = CVData
        fields = '__all__'