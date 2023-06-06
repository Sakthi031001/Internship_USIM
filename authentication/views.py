from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request,"authentication/home.html")

def register(request):    
    if request.method=='POST':
        name=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1==password2:        
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff=True
            user.is_superuser=False
            user.save()
            messages.success(request,'Your account has been created! You are able to login')
            return redirect('Login')
        else:
            messages.warning(request,'Password Mismatching...!!!')
            return redirect('Register')        
    else:
        form=CreateUserForm()        
        return render(request,"authentication/register.html",{'form':form})
    

@login_required
def profile(request):
    return render(request,"authentication/profile.html")
    



