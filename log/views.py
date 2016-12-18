from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, 'log/index.html')
    else:
        # form = LoginForm
        # return render(request, 'login.html', {'form': form})
        return redirect('login')


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            lastname = user_form.cleaned_data['lastname']
            firstname = user_form.cleaned_data['firstname']
            email = user_form.cleaned_data['email']
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']

            if User.objects.filter(username=username):
                return HttpResponse('existed')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=firstname, last_name=lastname)
                user.is_superuser = True
                user.is_staff = True
                user.save()
                user = authenticate(username=username, password=password)
                auth.login(request, user)
                return render(request, 'log/index.html')
        else:
            return render(request, 'log/failure.html', {'reason': user_form.errors})
    else:
        user_form = UserForm()
    return render(request, 'log/register.html', {'user_form': user_form})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if User.objects.filter(username=username):
                if user is not None and user.is_active:
                    auth.login(request, user)
                    response = render(request, 'log/index.html', {'form': login_form})
                    response.set_cookie('username', username, 3600)
                    return response
            else:
                return render(request, 'log/login.html', {'form': form})
        else:
            return render(request, 'log/login.html', {'form': form})
    return render(request, 'log/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('login')