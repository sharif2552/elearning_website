from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

# views.py

from django.shortcuts import render, redirect
from .forms import RegistrationForm

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form)
            user = form.save()
            print(form.cleaned_data)
            return redirect('/login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()
    
    return render(request, 'signup.html', {'form': form})


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        print(username, pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('/login/')

