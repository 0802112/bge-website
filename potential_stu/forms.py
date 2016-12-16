from django import forms
from django.forms import SelectDateWidget
from .models import PotentialStu, CounsellingInfo


class PotentialForm(forms.ModelForm):

    class Meta:
        model = PotentialStu
        fields = ('name', 'agent', 'dob', 'gender', 'phone', 'email', 'parent_phone',
                  'parent_email', 'city', 'state', 'school', 'grade', 'gpa', 'toefl')
        widgets = {
            'dob': SelectDateWidget(years=range(1990, 2016)),
        }


class CounsellingForm(forms.ModelForm):

    class Meta:
        model = CounsellingInfo
        fields = ('semester', 'apply_grade', 'school1', 'school2', 'school3',
                  'note', 'counsellor', 'date', 'status', 'fee', 'pay_date',)
        widgets = {
            'date': SelectDateWidget(years=range(2013, 2020)),
            'pay_date': SelectDateWidget(years=range(2013, 2020)),
        }


class ConfirmForm(forms.Form):
    CONFIRM_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    confirm = forms.ChoiceField(choices=CONFIRM_CHOICES, widget=forms.RadioSelect())