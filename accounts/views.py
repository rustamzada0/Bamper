from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import RegisterForm
from .models import User

# Create your views here.

def sign_in(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('accounts:profile'))
    else:
        error = ''
        if request.method == "POST":
            password = request.POST['password']
            if '@' in request.POST['emailornumber']:
                email = request.POST['emailornumber']
                user = authenticate(request, emailornumber = email, password = password)
                if user is not None: 
                    login(request,user)
                    return redirect(reverse_lazy("core:home"))
                else:  error=('Email or number or password wrong')              
            else:
                number = request.POST['emailornumber']
                user = User.objects.filter(emailornumber = number).first()
                if user is not None: 
                    login(request,user)
                    return redirect(reverse_lazy("core:home"))
                else:  error=('Email or number or password wrong')              
        return render(request, 'log-in.html', context={'error':error})


def sign_up(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('accounts:profile'))
    else:
        form = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.is_active = True #False
                user.save()


                return redirect(reverse_lazy('accounts:login'))
    return render(request, 'user-register.html', context={'form':form})

def change_password(request):
    return render(request, 'change-password.html')


@login_required()
def profile(request):
    return render(request, 'user-profile.html')


def logout_request(request):
    logout(request)
    return redirect('accounts:login')