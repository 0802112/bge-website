from django import forms
from django.forms import SelectDateWidget
from .models import StudentInfo, FatherInfo, MotherInfo, ContactInfo, AdditionalHousehold, SchoolInfo, TestScore, \
                    History, Profile, MultipleChoice, ShortAnswer


class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentInfo
        fields = ('firstname', 'lastname', 'middlename', 'englishname', 'dob', 'birthplace', 'apply_grade', \
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


class AdditionHousehodForm(forms.ModelForm):

    class Meta:
        model = AdditionalHousehold
        exclude = ['id']


class SchoolInfoForm(forms.ModelForm):

    class Meta:
        model = SchoolInfo
        exclude = ['id']


class TestScoreForm(forms.ModelForm):

    class Meta:
        model = TestScore
        exclude = ['id']


class HistoryForm(forms.ModelForm):

    class Meta:
        model = History
        exclude = ['id']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['id']


class MultiChoiceForm(forms.ModelForm):

    class Meta:
        model = MultipleChoice
        exclude = ['id']
        # widgets = {
        #     'personality': forms.CheckboxSelectMultiple,
        #     'eat': forms.CheckboxSelectMultiple,
        #     'not_eat': forms.CheckboxSelectMultiple,
        #     'special_diet': forms.CheckboxSelectMultiple,
        #     'allergy': forms.CheckboxSelectMultiple,
        #     'restaurant': forms.CheckboxSelectMultiple,
        #     'pet': forms.CheckboxSelectMultiple
        # }
        widgets = {
            'personality': forms.RadioSelect,
            'eat': forms.RadioSelect,
            'not_eat': forms.RadioSelect,
            'special_diet': forms.RadioSelect,
            'allergy': forms.RadioSelect,
            'restaurant': forms.RadioSelect,
            'pet': forms.RadioSelect,
        }


class ShortAnswerForm(forms.ModelForm):

    class Meta:
        model = ShortAnswer
        exclude = ['id']

