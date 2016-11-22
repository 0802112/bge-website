from django.shortcuts import render, HttpResponse
from .models import StudentInfo, FatherInfo, MotherInfo, ContactInfo
from .forms import StudentForm, FatherForm, MotherForm, ContactForm, ProfileForm, MultiChoiceForm, ShortAnswerForm
# Create your views here.


def stu_list(request):
    student_list = StudentInfo.objects.all()
    return render(request, 'current_stu/student_list.html', {'student_list': student_list})


def new_stu(requset):
    if requset.method == 'POST':
        form1 = StudentForm(requset.POST)
        form2 = FatherForm(requset.POST)
        form3 = MotherForm(requset.POST)
        form4 = ContactForm(requset.POST)

        if all((form1.is_valid(), form2.is_valid(), form3.is_valid(), form4.is_valid())):
            post1 = form1.save()
            post2 = form2.save(commit=False)
            post3 = form3.save(commit=False)
            post4 = form4.save(commit=False)
            post2.id = post1
            post3.id = post1
            post4.id = post1
            post2.save()
            post3.save()
            post4.save()
        else:
            return HttpResponse('wrong')
    else:
        form1 = StudentForm()
        form2 = FatherForm()
        form3 = MotherForm()
        form4 = ContactForm()
        form5 = ProfileForm()
        form6 = MultiChoiceForm()
        testform = ShortAnswerForm()

    return render(requset, 'current_stu/student_form.html', {'form1': form1, 'form2': form2, \
                                                                 'form3': form3, 'form4': form4, \
                                                                'form5': form5, 'form6': form6, 'testform': testform})
