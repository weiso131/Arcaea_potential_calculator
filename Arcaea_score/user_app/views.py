import logging

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import check_password

logger = logging.getLogger(__name__)

def check_user_exist(username):
    try:
        User.objects.get(username=username)
        return True
    except:
        return False

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect("/ptt_calculator")


    if request.method == 'GET':
        return render(request, 'user_app/login.html')
    else:
        
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/ptt_calculator')
        else:
            return render(request, 'user_app/login.html')


def logout(request):
    auth.logout(request)
    return redirect("/ptt_calculator")


def register(request):
    context = {}
    
    if request.method == "GET":
        return render(request, 'user_app/register.html', context)
    
    elif request.method == "POST":
        user_info = request.POST
        username = user_info['username']
        password = user_info['password']

        user_exist = check_user_exist(username)

    
        if user_exist:
            return render(request, 'user_app/register.html', context)
        else:
            user = User.objects.create_user(username=username, password=password)
            auth.login(request, user)
            return redirect("/ptt_calculator")
        
def edit_password(request):
    if not request.user.is_authenticated:
        return redirect("/ptt_calculator")
    if request.method == "GET":
        return render(request, 'user_app/edit_password.html', context={"wrong_password" : False})
    else:
        user = request.user
        password = request.POST['password']
        new_password = request.POST['new_password']

        if not check_password(password, user.password):
            return render(request, 'user_app/edit_password.html', context={"wrong_password" : True})
        else:
            user.set_password(new_password)
            user.save()
            auth.login(request, user)
            return redirect("/ptt_calculator")