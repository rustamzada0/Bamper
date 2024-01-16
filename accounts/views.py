from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.contrib import messages
from .tokens import account_activation_token
from .tasks import send_confirmation_mail
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


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # return redirect('accounts:login')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

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
                user.is_active = False
                user.save()
                send_confirmation_mail(user, get_current_site(request))
                messages.add_message(request, messages.SUCCESS, f"We sent an activation link to {user.emailornumber}. Please check your email.") 

                return redirect(reverse_lazy('accounts:profile'))
    return render(request, 'user-register.html', context={'form':form})


class ActiveAccountView(View):
    def get(request, *args, **kwargs):
        uidb64 = kwargs['uidb64']
        token = kwargs['token']
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect(reverse_lazy("accounts:login"))
        else:
            return render(request, 'activation.html')

def change_password(request):
    return render(request, 'change-password.html')


@login_required()
def profile(request):
    return render(request, 'user-profile.html')


def logout_request(request):
    logout(request)
    return redirect('accounts:login')