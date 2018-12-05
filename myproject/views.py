from django.shortcuts import render, redirect
import requests
import re
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
import dataset
from . import sql_py2
from django.contrib.auth.models import User
#import rhino


from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Это поле обязательно')



    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )



class SignInForm(UserCreationForm):


    class Meta:
        model = User
        fields = ('email', 'password', )


def vk_com(request):
    if request.method == "GET":
        t = requests.get("http://192.168.43.145:8888/v1/chain/get_info").json()
        resp = HttpResponse()
        resp.write(str(t))
        resp.status_code = 200
    return resp



def main(request):
    return render(request, "index.html")

def search(request):
    return render(request, "index_search.html")

def infort(request):
    if request.method == 'POST':
        #lisp = str(request.POST['list'])
        f = open('text.txt', 'w')
        f.write("cvxcv")
        f.close()
        resp = HttpResponse()
        resp.status_code = 200
        return resp


def comers(request):
    if request.method == "GET":
        f = open('text.txt', 'r')
        lisp = f.read()
        f.close()
        resp = HttpResponse()
        resp.write(str(lisp))
        resp.status_code = 200
    return resp

def signin(request):
    print(str(request.method)+"2")
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        if sql_py2.isLogin(username):
            if sql_py2.isPasswd(username, password):
                print("OK")
                return render(request, 'index-employee.html')
        #print(username)
        return redirect('/')
    else:
        form = SignInForm()
    return render(request, 'index_sig.html', {'form': form})

def form_r(request):
    if request.method == 'POST':
        #rhino /static/js/scatter.js
        return render(request, "index.html")
    else:
        form = SignInForm()
    return render(request, 'index_form.html', {'form': form})


def form2(request):
    #rhino /static/js/scatter.js
    return render(request, "index.html")

def register(request):
    print(str(request.method))
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("dsfsd")
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            my_password = form.cleaned_data.get('password1')
            sql_py2.regino(username, email, my_password)

            #user = authenticate(username=username, password=my_password)
            #login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'index_reg.html', {'form': form})



