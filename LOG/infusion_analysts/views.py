from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def register_1(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        if password == re_password:
            if User.objects.filter(username = username).exists():
                messages.error(request,'Username already exist')
                return render(request,'account/register.html')
            elif User.objects.filter(email = email).exists():
                messages.error(request,'email already exist')
                return render(request,'account/register.html')
            else:
                user=User.objects.create_user(first_name = first_name,last_name = last_name,username = username,email=email,password = password)
                user.save()
                return redirect('login1')
        else:
            messages.error(request,'password does not match')
            return render(request,'account/register.html')
    else:
        return render(request,'account/register.html')
    
def login_1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid credencials')
            return render(request,'account/login1.html')
    else:
        return render(request,'account/login1.html')

def logout_1(request):
    logout(request)                                                                                                                          
    return redirect('home')
def home_1(request):
    return render (request,'account/logout.html')


      

