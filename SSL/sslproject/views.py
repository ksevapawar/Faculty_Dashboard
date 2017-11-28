import re
import urllib

from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from sslproject.Crawler.Awards import *
from sslproject.models import Employee, Teaching, Publication, Education, Projects, Achievements
from sslproject.forms import SignUpForm, EditProfileForm, EditProfileForm2, SignUpForm2, Teachingform, Publicationform, \
    Educationform, Projectsform, Achievementsform, SearchForm, WebsiteForm
# Create your views here.

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
import urllib.request

@login_required(login_url='/login')
def index(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            website = cleaned_data['website']
            page = urllib.request.urlopen(website).read()
            html = BeautifulSoup(str(page), "lxml")
            achieve(request, html)
            pjt(request,html)
            publ(request,html)
            teach(request,html)
            meta_data(request,html)
            educate(request,html)

        return redirect('/accounts/profile/')

    else:
        return render(request, 'dashboard/index.html')

def user_table(request):
       return render(request, 'dashboard/teaching.html')

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
            return render(request, 'signup.html', {'form_errors': form.errors})

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
        return render(request,'dashboard/teaching.html',{'Teaching':Teaching.objects.filter(user=request.user.id)})

def publication(request):
    if request.method == 'POST':
        form = Publicationform(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            p = Publication(user=request.user);
            p.pub  = cleaned_data['pub']
            p.where = cleaned_data['where']
            p.save()
        return redirect('/accounts/profile/publication/')

    else:
        return render(request, 'dashboard/publication.html', {'Publication': Publication.objects.filter(user=request.user.id)})

def education(request):
    if request.method == 'POST':
        form = Educationform(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            edu = Education(user=request.user);
            edu.degree  = cleaned_data['degree']
            edu.department = cleaned_data['department']
            edu.institute = cleaned_data['institute']
            edu.year = cleaned_data['year']
            edu.country = cleaned_data['country']
            edu.save()
        return redirect('/accounts/profile/education/')

    else:
        return render(request, 'dashboard/education.html', {'Education': Education.objects.filter(user=request.user.id)})

def projects(request):
    if request.method == 'POST':
        form = Projectsform(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            pro = Projects(user=request.user);
            pro.title  = cleaned_data['title']
            pro.sponser = cleaned_data['sponser']
            pro.duration = cleaned_data['duration']
            pro.role = cleaned_data['role']
            pro.save()
        return redirect('/accounts/profile/projects/')

    else:
        return render(request, 'dashboard/projects.html', {'Projects': Projects.objects.filter(user=request.user.id)})





def achievements(request):
    if request.method == 'POST':
        form = Achievementsform(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            a = Achievements(user=request.user);
            a.year  = cleaned_data['year']
            a.ach = cleaned_data['ach']
            a.details = cleaned_data['details']
            a.save()
        return redirect('/accounts/profile/achievements/')

    else:
        return render(request, 'dashboard/achievements.html', {'Achievements': Achievements.objects.filter(user=request.user.id)})


def function(request,part_id =None):
    object = Teaching.objects.get(id=part_id)
    object.delete()
    return redirect('/accounts/profile/table/')
   # return render(request,'/accounts/profile/table/'

def function2(request,part_id =None):
    object = Publication.objects.get(id=part_id)
    object.delete()
    return redirect('/accounts/profile/publication/')

def function3(request,part_id =None):
    object = Education.objects.get(id=part_id)
    object.delete()
    return redirect('/accounts/profile/education/')

def function4(request,part_id =None):
    object = Projects.objects.get(id=part_id)
    object.delete()
    return redirect('/accounts/profile/projects/')

def function5(request,part_id =None):
    object = Achievements.objects.get(id=part_id)
    object.delete()
    return redirect('/accounts/profile/achievements/')


def show_main(request,username= None):
    user=User.objects.get(username=username)
    teach=Teaching.objects.filter(user=user.id)
    edu=Education.objects.filter(user=user.id)
    publication = Publication.objects.filter(user= user.id)
    achievements = Achievements.objects.filter(user=user.id)
    return render(request, 'profile/personal_page.html',{'user':user,'teaching':teach,'education':edu,'publications':publication,'achievements':achievements,})

def find_user_by_name(request):
    form = SearchForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            cleaned_data = form.cleaned_data
            query_name = cleaned_data['query']
            qs = User.objects.all()
            for term in query_name.split():
                qs = qs.filter( Q(first_name__icontains = term) | Q(last_name__icontains = term))

            return render(request,'main/search.html',{'results':qs  })
        else:
            return render(request,'main/search.html')
    else:
        return render(request,'main/search.html')

