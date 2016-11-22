from django import forms
from django.forms import SelectDateWidget
from .models import StudentInfo, FatherInfo, MotherInfo, ContactInfo, Profile, MultipleChoice, ShortAnswer


class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentInfo
        fields = ('test', 'firstname', 'lastname', 'middlename', 'englishname', 'dob', 'birthplace', 'apply_grade', \
                  'start_date', 'visa', 'nation', 'i20',)
        widgets = {
            'dob': SelectDateWidget,
        }


class FatherForm(forms.ModelForm):

    class Meta:
        model = FatherInfo
        fields = ('lastname', 'firstname', 'marital', 'occupation', 'employer', 'education', \
                  'day_phone', 'email')


class MotherForm(forms.ModelForm):

    class Meta:
        model = MotherInfo
        fields = ('lastname', 'firstname', 'marital', 'occupation', 'employer', 'education', \
                  'day_phone', 'email')


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactInfo
        fields = ('address', 'apt', 'city', 'state', 'country', 'postcode', 'home_phone', 'mobile_phone', \
                  'fax', 'email',)


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'


class MultiChoiceForm(forms.ModelForm):

    class Meta:
        model = MultipleChoice
        exclude = ['id']
        widgets = {
            'personality': forms.CheckboxSelectMultiple,
            'eat': forms.CheckboxSelectMultiple,
            'not_eat': forms.CheckboxSelectMultiple,
            'special_diet': forms.CheckboxSelectMultiple,
            'allergy': forms.CheckboxSelectMultiple,
            'restaurant': forms.CheckboxSelectMultiple,
            'pet': forms.CheckboxSelectMultiple
        }


class ShortAnswerForm(forms.ModelForm):

    class Meta:
        model = ShortAnswer
        exclude = ['id']

