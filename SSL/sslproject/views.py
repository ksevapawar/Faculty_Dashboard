from django.contrib.auth.models import User
from django.shortcuts import render
from sslproject.models import Employee
from sslproject.forms import SignUpForm, EditProfileForm, EditProfileForm2, SignUpForm2
# Create your views here.

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):
    return render(request, 'dashboard/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # form2=SignUpForm2(request.POST,instance=request.user.employee)
        if form.is_valid():
            form.save()
        # if form2.is_valid():
        #     form2.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
           # u= User.objects.get(username=username)

            #m=Employee.objects.get(user__username=username)
            #m.department=form.cleaned_data.get('department')
            #m.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/login')

def user(request):
    return render(request, 'dashboard/user.html')

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        form2 = EditProfileForm2(request.POST,request.FILES, instance=request.user.employee)
        if form.is_valid():
            form.save()
        if form2.is_valid():
            form2.save()
        return redirect('/accounts/profile/user')

    else:

        return render(request, 'dashboard/user.html')