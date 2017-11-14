from django.contrib.auth.models import User
from django.shortcuts import render
from sslproject.models import Employee, Teaching, Publication
from sslproject.forms import SignUpForm, EditProfileForm, EditProfileForm2, SignUpForm2, Teachingform, Publicationform
# Create your views here.

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):
    return render(request, 'dashboard/index.html')

def user_table(request):
    return render(request, 'dashboard/table.html')

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

def teaching(request):
    if request.method == 'POST':
        form = Teachingform(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            teach = Teaching(user=request.user);
            teach.course=cleaned_data['course']
            teach.start_date=cleaned_data['start_date']
            teach.end_date=cleaned_data['end_date']
            #form = Teachingform(request.POST,instance=teach)
            #teach.course = form.course
            #if form.is_valid():
            teach.save()
        return redirect('/accounts/profile/table/')

    else :
        return render(request,'dashboard/table.html',{'Teaching':Teaching.objects.filter(user=request.user.id)})

def publication(request):
    if request.method == 'POST':
        form = Publicationform(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            p = Publication(user=request.user);
            p.pub  = cleaned_data['pub']
            p.save()
        return redirect('/accounts/profile/publication/')

    else:
        return render(request, 'dashboard/typography.html', {'Publication': Publication.objects.filter(user=request.user.id)})

def function(request,part_id =None):
    object = Teaching.objects.get(id=part_id)
    object.delete()
    return redirect('/accounts/profile/table/')
   # return render(request,'/accounts/profile/table/'

def function2(request,part_id =None):
    object = Publication.objects.get(id=part_id)
    object.delete()
    return redirect('/accounts/profile/publication/')
