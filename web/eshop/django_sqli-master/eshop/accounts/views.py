from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.

def login_req(r):
    if r.user.is_authenticated:
        return redirect('app/index')
    if r.method=='POST':
        username = r.POST['username']
        password = r.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(r,user)
            return redirect('index')
        else:
            return render(r,'login.html',{
                'error':"Wrong credidentals."
            })
    else:
        return render(r,'login.html')

def register_req(r):
    if r.method=='POST':
        username = r.POST['username']
        password = r.POST['password']
        email = r.POST['email']
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('login')
        else:
            return render(r,'register.html',{
                'error': "User already exists."
            })
    else:
        return render(r,'register.html')


def logout_req(r):
    logout(r)
    return redirect('index')