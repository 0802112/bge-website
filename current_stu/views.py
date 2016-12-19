from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django import forms
from .models import StudentInfo, FatherInfo, MotherInfo, ContactInfo, AdditionalHousehold, SchoolInfo, TestScore, \
                    History, Profile, MultipleChoice, ShortAnswer

from .forms import StudentForm, FatherForm, MotherForm, ContactForm, AdditionHousehodForm, SchoolInfoForm, \
                                TestScoreForm, HistoryForm, ProfileForm, MultiChoiceForm, ShortAnswerForm
# Create your views here.


# def stu_list(request):
#     student_list = StudentInfo.objects.all()
#     return render(request, 'current_stu/student_list.html', {'student_list': student_list})



class ConfirmForm(forms.Form):
    CONFIRM_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    confirm = forms.ChoiceField(choices=CONFIRM_CHOICES, widget=forms.RadioSelect())

# ======================================


def stu_list(request, template_name='current_stu/student_list.html'):
    student_list = StudentInfo.objects.all()
    return render(request, template_name, {'student_list': student_list})


def new_stu(request):
    if request.method == 'POST':
        form1 = StudentForm(request.POST)
        form2 = FatherForm(request.POST)
        form3 = MotherForm(request.POST)
        form4 = ContactForm(request.POST)
        form5 = AdditionHousehodForm(request.POST)
        form6 = SchoolInfoForm(request.POST)
        form7 = TestScoreForm(request.POST)
        form8 = HistoryForm(request.POST)
        form9 = ProfileForm(request.POST)
        form10 = MultiChoiceForm(request.POST)
        form11 = ShortAnswerForm(request.POST)

        if all((form1.is_valid(), form2.is_valid(), form3.is_valid(), form4.is_valid(), form5.is_valid(),
                form6.is_valid(), form7.is_valid(), form8.is_valid(), form9.is_valid(), form10.is_valid(),
                form11.is_valid())):
            post1 = form1.save()
            post2 = form2.save(commit=False)
            post3 = form3.save(commit=False)
            post4 = form4.save(commit=False)
            post5 = form5.save(commit=False)
            post6 = form6.save(commit=False)
            post7 = form7.save(commit=False)
            post8 = form8.save(commit=False)
            post9 = form9.save(commit=False)
            post10 = form10.save(commit=False)
            post11 = form11.save(commit=False)

            post2.id = post1
            post3.id = post1
            post4.id = post1
            post5.id = post1
            post6.id = post1
            post7.id = post1
            post8.id = post1
            post9.id = post1
            post10.id = post1
            post11.id = post1

            post2.save()
            post3.save()
            post4.save()
            post5.save()
            post6.save()
            post7.save()
            post8.save()
            post9.save()
            post10.save()
            post11.save()
        else:
            return HttpResponse('wrong')
    else:
        form1 = StudentForm()
        form2 = FatherForm()
        form3 = MotherForm()
        form4 = ContactForm()
        form5 = AdditionHousehodForm()
        form6 = SchoolInfoForm()
        form7 = TestScoreForm()
        form8 = HistoryForm()
        form9 = ProfileForm()
        form10 = MultiChoiceForm()
        form11 = ShortAnswerForm()

    return render(request, 'current_stu/student_form.html', {'form1': form1, 'form2': form2, 'form3': form3,
                                                             'form4': form4, 'form5': form5, 'form6': form6,
                                                             'form7': form7, 'form8': form8, 'form9': form9,
                                                             'form10': form10, 'form11': form11})


def detail_stu(request, pk, template_name='current_stu/student_detail.html'):
    student = get_object_or_404(StudentInfo, pk=pk)
    father = get_object_or_404(FatherInfo, pk=pk)
    mother = get_object_or_404(MotherInfo, pk=pk)
    contact = get_object_or_404(ContactInfo, pk=pk)
    additional = get_object_or_404(AdditionalHousehold, pk=pk)
    school = get_object_or_404(SchoolInfo, pk=pk)
    test = get_object_or_404(TestScore, pk=pk)
    history = get_object_or_404(History, pk=pk)
    profile = get_object_or_404(Profile, pk=pk)
    multichoice = get_object_or_404(MultipleChoice, pk=pk)
    shortanswer = get_object_or_404(ShortAnswer, pk=pk)

    return render(request, template_name, {'student': student, 'father': father, 'mother': mother, 'contact': contact,
                                           'additional': additional, 'school': school, 'test': test, 'history': history,
                                           'profile': profile, 'multichoice': multichoice, 'shortanswer': shortanswer
                                          })


def update_stu(request, pk, template_name='current_stu/student_form.html'):
    student = get_object_or_404(StudentInfo, pk=pk)
    father = get_object_or_404(FatherInfo, pk=pk)
    mother = get_object_or_404(MotherInfo, pk=pk)
    contact = get_object_or_404(ContactInfo, pk=pk)
    additional = get_object_or_404(AdditionalHousehold, pk=pk)
    school = get_object_or_404(SchoolInfo, pk=pk)
    test = get_object_or_404(TestScore, pk=pk)
    history = get_object_or_404(History, pk=pk)
    profile = get_object_or_404(Profile, pk=pk)
    multichoice = get_object_or_404(MultipleChoice, pk=pk)
    shortanswer = get_object_or_404(ShortAnswer, pk=pk)

    if request.method == 'POST':
        form1 = StudentForm(request.POST, instance=student)
        form2 = FatherForm(request.POST, instance=father)
        form3 = MotherForm(request.POST, instance=mother)
        form4 = ContactForm(request.POST, instance=contact)
        form5 = AdditionHousehodForm(request.POST, instance=additional)
        form6 = SchoolInfoForm(request.POST, instance=school)
        form7 = TestScoreForm(request.POST, instance=test)
        form8 = HistoryForm(request.POST, instance=history)
        form9 = ProfileForm(request.POST, instance=profile)
        form10 = MultiChoiceForm(request.POST, instance=multichoice)
        form11 = ShortAnswerForm(request.POST, instance=shortanswer)

        if all((form1.is_valid(), form2.is_valid(), form3.is_valid(), form4.is_valid(), form5.is_valid(),
                form6.is_valid(), form7.is_valid(), form8.is_valid(), form9.is_valid(), form10.is_valid(),
                form11.is_valid())):
            post1 = form1.save()
            post2 = form2.save(commit=False)
            post3 = form3.save(commit=False)
            post4 = form4.save(commit=False)
            post5 = form5.save(commit=False)
            post6 = form6.save(commit=False)
            post7 = form7.save(commit=False)
            post8 = form8.save(commit=False)
            post9 = form9.save(commit=False)
            post10 = form10.save(commit=False)
            post11 = form11.save(commit=False)

            post2.id = post1
            post3.id = post1
            post4.id = post1
            post5.id = post1
            post6.id = post1
            post7.id = post1
            post8.id = post1
            post9.id = post1
            post10.id = post1
            post11.id = post1

            post2.save()
            post3.save()
            post4.save()
            post5.save()
            post6.save()
            post7.save()
            post8.save()
            post9.save()
            post10.save()
            post11.save()

            return redirect('stu_list')

    else:
        form1 = StudentForm(instance=student)
        form2 = FatherForm(instance=father)
        form3 = MotherForm(instance=mother)
        form4 = ContactForm(instance=contact)
        form5 = AdditionHousehodForm(instance=additional)
        form6 = SchoolInfoForm(instance=school)
        form7 = TestScoreForm(instance=test)
        form8 = HistoryForm(instance=history)
        form9 = ProfileForm(instance=profile)
        form10 = MultiChoiceForm(instance=multichoice)
        form11 = ShortAnswerForm(instance=shortanswer)

    return render(request, template_name, {'form1': form1, 'form2': form2, 'form3': form3,
                                                             'form4': form4, 'form5': form5, 'form6': form6,
                                                             'form7': form7, 'form8': form8, 'form9': form9,
                                                             'form10': form10, 'form11': form11})


def delete_stu(request, pk, template_name='delete_confirm.html'):
    student = get_object_or_404(StudentInfo, pk=pk)
    if request.method == 'POST':
        if request.POST['choice'] == 'yes':
            student.delete()
            return redirect('stu_list')
        else:
            return HttpResponse('Fail')

    else:
        form = ConfirmForm()
    return render(request, template_name, {'form': form})










































