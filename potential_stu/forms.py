from django import forms
from django.forms import SelectDateWidget
from .models import PotentialStu, CounsellingInfo


class PotentialForm(forms.ModelForm):

    class Meta:
        model = PotentialStu
        fields = ('name', 'agent', 'dob', 'gender', 'phone', 'email', 'parent_phone', \
                  'parent_email', 'city', 'state', 'school', 'grade', 'gpa',)
        widgets = {
            'dob': SelectDateWidget,
        }


class CounsellingForm(forms.ModelForm):

    class Meta:
        model = CounsellingInfo
        fields = ('semester', 'apply_grade', 'school1', 'school2', 'school3', \
                  'note', 'counsellor', 'date', 'status', 'fee', 'pay_date',)