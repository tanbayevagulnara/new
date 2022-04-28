from django.shortcuts import redirect, render
from .forms import User_Form
from .models import *
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages import constants

# Create your views here.


def first(request):
    send_mail('Hello from Gulnara', 
    'Hello, this is Gulnara!', 
    '200103501@stu.sdu.edu.kz', 
    ['gulnaratanbayeva@gmail.com'], 
    fail_silently=True)

    return render(request, 'my_app/first.html')


def home(request):
    return render(request, 'my_app/home.html')


def register_request(request):
    if request.method == 'POST':
        form = User_Form(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Message')
            return redirect("my_app:home")
        
        messages.error(request, "registration failed, please try again")
    
    form = User_Form

    return render(request, 'my_app/register.html', context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.add_message(request, constants.SUCCESS, 'Message')
                return redirect("my_app:home")
            else:
                messages.error(request, "please, try again")

        else: 
            messages.error(request, "please, try again")
        
    form = AuthenticationForm()

    return render(request, 'my_app/login.html', context={'login_form': form})




def main(request):
    return render(request, 'my_app/main.html')