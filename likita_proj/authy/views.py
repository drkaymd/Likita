from django.shortcuts import render, redirect
from django.http import HttpResponse
from base.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm
from django.contrib import messages
from profiles.forms import ProfileForm

from verify_email.email_handler import send_verification_email


# Create your views here.
def register(request):
    page = 'register'      
    form = MyUserCreationForm()
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'Email aleady Exists')
                              
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.warning(request, 'User aleady Exists')
                return redirect('register')
                
            else:
                form = MyUserCreationForm(request.POST)
                if form.is_valid():
                    inactive_user = send_verification_email(request, form)
                    inactive_user.username = inactive_user.username.upper()
                    inactive_user.email = inactive_user.email.lower()
                    messages.success(request, f'Account created for {inactive_user.username} successfully!. Kindly check you email "<strong> {inactive_user.email} </strong>" to activate your account')
                    # return redirect('settings', pk=user.username)

        else:
            messages.error(request, 'Passwords Does Not Match')
            return redirect('register')
            
    
    context={'form': form, 'page': page}
    return render(request, 'authy/login-register.html', context)


def user_login(request):
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'{user} is successfully logged In!')            
            return redirect('profile', pk=user.username)
        
        else:
            messages.info(request, 'Credentials Invalid!, Please enter the correct email and password. Note that both fields may be case-sensitive.')
            return redirect('login')
    context={}
    return render(request, 'authy/login-register.html', context)

      
@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.success(request, f'You are successfully logged Out!')
    return redirect('home')

  
@login_required(login_url='login')  
def settings(request, pk):
    user = User.objects.get(username=pk)
    form = ProfileForm(instance=user)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect(f'/profile/{user.username}')
    
    context={'form':form, 'user': user}
    return render(request, 'authy/settings.html', context)

