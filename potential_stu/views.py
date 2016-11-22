from django.shortcuts import render, get_object_or_404, redirect
from .models import PotentialStu, CounsellingInfo
from .forms import PotentialForm, CounsellingForm


# Create your views here.
def stu_list(request):
    student_list = PotentialStu.objects.all()
    return render(request, 'potential_stu/student_list.html', {'student_list': student_list})


def new_stu(request):
    if request.method == 'POST':
        form1 = PotentialForm(request.POST)
        form2 = CounsellingForm(request.POST)
        if all((form1.is_valid(), form2.is_valid())):
            post1 = form1.save()
            post2 = form2.save(commit=False)
            post2.id = post1
            post2.save()
    else:
        form1 = PotentialForm()
        form2 = CounsellingForm()
    return render(request, 'potential_stu/student_form.html', {'form1': form1, 'form2': form2})


def update_stu(request, pk):
    stu = get_object_or_404(PotentialStu, pk=pk)
    consult = get_object_or_404(CounsellingInfo, pk=pk)
    if request.method == 'POST':
        form1 = PotentialForm(request.POST, instance=stu)
        form2 = CounsellingForm(request.POST, instance=consult)
        if all((form1.is_valid(), form2.is_valid())):
            post1 = form1.save()
            post2 = form2.save(commit=False)
            post2.id = post1
            post2.save()
            return redirect('stu_list')
    else:
        form1 = PotentialForm(instance=stu)
        form2 = CounsellingForm(instance=consult)
    return render(request, 'potential_stu/student_form.html', {'form1': form1, 'form2': form2})


def delete_stu(request, pk):
    stu = get_object_or_404(PotentialStu, pk=pk)
    consult = get_object_or_404(CounsellingInfo, pk=pk)
    if request.method == 'POST':
        stu.delete()
        return redirect('stu_list')
    return render(request, 'potential_stu/student_delete_confirm.html', {'object': stu})


def detail_stu(request, pk):
    student = get_object_or_404(PotentialStu, pk=pk)
    return render(request, 'potential_stu/student_detail.html', {'student': student})
#
#
# def post_detail(request, pk):
#     post = get_object_or_404(Potential_Basic, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})