from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UpdateProfileForm
from .models import Profile

@login_required(login_url='login-register')
def profile(request):
    cur_profile = request.user.profile
    context = {
        'user': cur_profile,
    }
    return render(request, 'users/profile.html', context)

def login_register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, 'User does not exists')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Username or password invalid')

    return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    return redirect('main-page')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('profile')

    page = 'register'
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = user.username
        user.save()

        login(request, user)
        return redirect('profile')

    context = {'page': page,
               'form': form,

               }
    return render(request, 'users/login.html', context)


@login_required(login_url='login-register')
def edit_account_info(request):
    cur_profile = request.user.profile
    form = UpdateProfileForm(instance=cur_profile)

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=cur_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            messages.error(request, 'Invalid input')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)