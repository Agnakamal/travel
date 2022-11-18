from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method =='POST':
        u = request.POST['username']
        p = request.POST['password']
        user=auth.authenticate(username=u,password=p)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalide credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        u = request.POST['username']
        f = request.POST['firstname']
        l = request.POST['lastname']
        e = request.POST['email']
        p = request.POST['password']
        c = request.POST['cpassword']
        if p==c:
            if User.objects.filter(username=u).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=e).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')