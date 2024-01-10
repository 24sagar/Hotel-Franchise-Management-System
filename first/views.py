from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



def aboutUs(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def services(request):
    return render(request,"services.html")

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get("pass")
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect('login')
    return render(request,"login.html")

@login_required(login_url='login')
def index(request):
    # data ={
    #     'title':'Index'
    # }
    return render(request,"index.html")


def Signup(request):
    if request.method =='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return redirect('signup')

        my_user= User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')

    return render(request,"signup.html")



def Logout(request):
    logout(request)
    return redirect('index')