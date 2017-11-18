import urllib.request
from urllib import request
import re
from bs4 import BeautifulSoup
from django.contrib.auth.models import User

from sslproject.models import Achievements, Projects, Publication, Teaching, Education


def achieve(request,html):
   # page = urllib.request.urlopen(u).read()
   # html = BeautifulSoup(page, "lxml")

    for awards in html.find_all('div',attrs={'fadeinup':'','anclassimated':'','data-content':'7'}  ):
       for t in awards('p', {'align': 'justify'}):
           a = Achievements(user=request.user)
           a.ach = t.text
           y = re.search(r"(\d{4})", t.text).group(1)
           a.year = y
           a.save()
    #return arr

def pjt(request,html):
    for city in html.find_all('p', {'align' : 'justify'}):
        a=city
        a=str(a)
        if "Project Title:" in a:
            p = Projects(user=request.user)
            p.title = ' '.join(re.findall(r'Project Title:</strong>(.+?)<br/>', a))
            p.sponser = ' '.join(re.findall(r'Funding Agency:</strong>(.+?)<br/>', a))
            p.duration = ' '.join(re.findall(r'Start Year:</strong>(.+?)<br/>',a)) + "-" + ' '.join(re.findall(r'End Year:</strong>(.+?)<br/>',a))
            p.save()

def publ(request,html):
    pub = []
    a = ""
    for city in html.find_all('div', attrs={'data-content': '5'}):
        for j in city('li'):
            for o in j('p', {'align': 'justify'}):
                 arr = " ".join(re.findall(r'".+"', o.text))
                 arr2 = " ".join(re.findall(r'",(.+)', o.text))
                 pu = Publication(user=request.user)
                 pu.pub = arr
                 pu.where = arr2
                 pu.save()


def teach(request,html):
    for city in html.find_all('div', {'class': 'fh5co-text'}):
        for t in city('li'):
            s = t.text.replace('&diam', '-').replace(';', '')
            e = re.split('⋄ |:|-',s)
            t =Teaching(user=request.user)
            t.course = e[3] + '(' + e[4] + ')'
            t.start_date = e[0]
            t.end_date = e[1]
            t.save()

def meta_data(request,html):
    labels = []
    data = []
    for city in html.find_all('div', {'class': 'fh5co-content-inner text-center'}):
        for item in city('div', {'class': 'col-md-3'}):
            for j in item('p'):
                data.append(j.text)
            for j in item('label'):
                labels.append(j.text)

    designation = data[0].split(",")[0].strip()
    department = data[0].split(",")[1].strip()
    email = re.search(r'([\w\.-]+ @ [\w\.-]+)', data[1]).group(0)
    phone_number = re.search(r'(\d{3} \d+)', data[1]).group(0)
    # room_number = re.search(r'Room No.: (.+)', data[1]).group(0)
    name = labels[0]
    name = name.split(" ")
    if (len(name) == 1):
        last_name = " "
        first_name = name[0]
    else:
        last_name = name[-1]
        first_name = ' '.join(name[0:-1])
    user=User.objects.get(username=request.user)
    user.employee.department = department
    user.employee.designation = designation
    user.employee.mobileNo = phone_number
    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.employee.save()
    user.save()

def educate(request,html):
    edu=[]
    a=""
    for city in html.find_all('div', {'class': 'fh5co-content-inner text-center'}):
        for item in city('div', {'class': 'fh5co-icon'}):
            for j in item('p'):
                if j.text:
                    arr = " ".join(re.findall(r'(.+)?\\n', j.text))
                    arr2=" ".join(re.findall(r',(.+),',j.text))
                    arr3=" ".join(re.findall(r'[0-9]{4}',j.text))
                    arr4 = " ".join(re.findall(r'\\t([^\\t].*),', j.text))
                    e = Education(user=request.user)
                    e.degree = arr
                    e.department = arr4
                    e.year = arr3
                    e.institute = arr2
                    e.country="India"
                    e.save()


#u='http://jatinga.iitg.ernet.in/cseintranet/intranet-pages/jatin'
#p=achievements(u)
#print(p)


