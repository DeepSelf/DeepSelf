from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django import template

register = template.Library()

@register.simple_tag
def call_method(obj, method_name, *args):
    method = getattr(obj, method_name)
    return method(*args)

def login_view(request):
    '''
    returns a page wich allows collaborator to get connected
    '''

    error = False

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # We verify if the sent data is correct
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = LoginForm()

    return render(request, 'login.html', locals())

def register(request):
    pass

def logout_view(request):
    '''
    logout the user then returns to the login view
    '''
    
    logout(request)
    return redirect('login')
    