from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect ,HttpResponseRedirect,HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
# Create your views here.

# views.py

from django.shortcuts import render, redirect
from .forms import RegistrationForm

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            print(form.cleaned_data)
            return redirect('/login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()
    
    return render(request, 'signup.html', {'form': form})


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Redirect to the originally requested URL or a default URL if 'next' is not provided
            redirect_url = request.GET.get('next', reverse('newapp:home'))
            return HttpResponseRedirect(redirect_url)
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'custom_login.html')

def LogoutPage(request):
    logout(request)
    return redirect('/login/')

