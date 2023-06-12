from django.shortcuts import render, redirect
from first_app.forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.


def home(request):

    return render(request, 'home.html')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                # messages.warning(request, 'warning')
                # messages.info(request, 'information')
                form.save()
                print(form.cleaned_data)
        else:
            form = RegisterForm()
        return render(request, 'signup.html', {'Form': form})
    else:
        return redirect('profile')


def Userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                # To check user is available in database
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    login(request, user)
                    return redirect('profile')  # Profile page a redirect korba
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                # messages.warning(request, 'warning')
                # messages.info(request, 'information')
                form.save()
                print(form.cleaned_data)
        else:
            form = ChangeUserData(instance=request.user)
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('signup')


def user_logout(request):
    logout(request)
    return redirect('login')

# Change password using old password:


def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'passchange.html', {'form': form})
    else:
        return redirect('login')

# Change password without old password:


def pass_changewithoutOldPass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'passchange.html', {'form': form})
    else:
        return redirect('login')


def Change_User_Data(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUserData(request.POST)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                # messages.warning(request, 'warning')
                # messages.info(request, 'information')
                form.save()
                print(form.cleaned_data)
        else:
            form = ChangeUserData()
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('signup')
