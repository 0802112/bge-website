from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django import forms
from django.forms import ModelForm
from .models import HostName, HostFather, HostMother, Contact, Additional

# =============== Forms =================

class HostNameForm(ModelForm):
    class Meta:
        model = HostName
        exclude = ['id']


class HostFatherForm(ModelForm):
    class Meta:
        model = HostFather
        exclude = ['id']


class HostMotherForm(ModelForm):
    class Meta:
        model = HostMother
        exclude = ['id']


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['id']


class AdditionalForm(ModelForm):
    class Meta:
        model = Additional
        exclude = ['id']


class ConfirmForm(forms.Form):
    CONFIRM_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    confirm = forms.ChoiceField(choices=CONFIRM_CHOICES, widget=forms.RadioSelect())


# ============== Home ===================

def home(request, template_name='host_family/home.html'):
    hostname = HostName.objects.all()
    # hostfather = HostFather.objects.all()
    # hostmather = HostMother.objects.all()
    # contact = Contact.objects.all()
    # additional = Additional.objects.all()

    return render(request, template_name, {'host_list': hostname})


# ============== CRUD ===================


def new_host(request, template_name='host_family/host_form.html'):
    if request.method == 'POST':
        form1 = HostNameForm(request.POST)
        form2 = HostFatherForm(request.POST)
        form3 = HostMotherForm(request.POST)
        form4 = ContactForm(request.POST)
        form5 = AdditionalForm(request.POST)

        if all((form1.is_valid(), form2.is_valid(), form3.is_valid(), form4.is_valid(), form5.is_valid())):
            post1 = form1.save()
            post2 = form2.save(commit=False)
            post3 = form3.save(commit=False)
            post4 = form4.save(commit=False)
            post5 = form5.save(commit=False)
            post2.id = post1
            post3.id = post1
            post4.id = post1
            post5.id = post1
            post2.save()
            post3.save()
            post4.save()
            post5.save()
        else:
            return HttpResponse('wrong')

    else:
        form1 = HostNameForm()
        form2 = HostFatherForm()
        form3 = HostMotherForm()
        form4 = ContactForm()
        form5 = AdditionalForm()

    return render(request, template_name, {'form1': form1, 'form2': form2, 'form3': form3,\
                                           'form4': form4, 'form5': form5})


def detail_host(request, pk, template_name='host_family/host_detail.html'):
    host = get_object_or_404(HostName, pk=pk)
    father = get_object_or_404(HostFather, pk=pk)
    mother = get_object_or_404(HostMother, pk=pk)
    contact = get_object_or_404(Contact, pk=pk)
    additional = get_object_or_404(Additional, pk=pk)
    return render(request, template_name, {'host': host, 'father': father, 'mother': mother,
                                           'contact': contact, 'additional': additional})


def update_host(request, pk, template_name='host_family/host_form.html'):
    host = get_object_or_404(HostName, pk=pk)
    father = get_object_or_404(HostFather, pk=pk)
    mother = get_object_or_404(HostMother, pk=pk)
    contact = get_object_or_404(Contact, pk=pk)
    additional = get_object_or_404(Additional, pk=pk)

    if request.method == 'POST':
        form1 = HostNameForm(request.POST, instance=host)
        form2 = HostFatherForm(request.POST, instance=father)
        form3 = HostMotherForm(request.POST, instance=mother)
        form4 = ContactForm(request.POST, instance=contact)
        form5 = AdditionalForm(request.POST, instance=additional)
        if all((form1.is_valid(), form2.is_valid(), form3.is_valid(), form4.is_valid(), form5.is_valid())):
            post1 = form1.save()
            post2 = form2.save(commit=False)
            post3 = form3.save(commit=False)
            post4 = form4.save(commit=False)
            post5 = form5.save(commit=False)
            post2.id = post1
            post3.id = post1
            post4.id = post1
            post5.id = post1
            post2.save()
            post3.save()
            post4.save()
            post5.save()
            return redirect('host_list')
    else:
        form1 = HostNameForm(instance=host)
        form2 = HostFatherForm(instance=father)
        form3 = HostMotherForm(instance=mother)
        form4 = ContactForm(instance=contact)
        form5 = AdditionalForm(instance=additional)
    return render(request, template_name, {'form1': form1, 'form2': form2, 'form3': form3,
                                           'form4': form4, 'form5': form5})


def delete_host(request, pk, template_name='host_family/host_delete_confirm.html'):
    host = get_object_or_404(HostName, pk=pk)
    if request.method == 'POST':
        if request.POST['choice'] == 'yes':
            host.delete()
            return redirect('host_list')
        else:
            return HttpResponse('Fail')

    else:
        form = ConfirmForm()
    return render(request, template_name, {'form': form})



























