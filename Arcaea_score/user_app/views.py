from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth


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