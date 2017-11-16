import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from sslproject.models import Employee, Teaching, Publication, Education, Projects, Achievements


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class SignUpForm2(forms.ModelForm):
    department=forms.CharField(max_length=30, required=False)
    mobileNo = forms.CharField(max_length=30, required=False)
    designation = forms.CharField(max_length=30, required=False)
    gender = forms.CharField(max_length=30, required=False)
    currentinstitute = forms.CharField(max_length=30, required=False)
    year = forms.CharField(max_length=30, required=False)
    address = forms.CharField(max_length=30, required=False)

    class Meta:
        model = Employee
        fields=('department','mobileNo','designation','gender','currentinstitute','year','address')

class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, help_text='Optional.')
    last_name = forms.CharField(max_length=30 , help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # department = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')



class EditProfileForm2(forms.ModelForm):

    department = forms.CharField(max_length=30 , help_text='Optional.')
    mobileNo = forms.CharField(max_length=30, help_text='Optional.')
    designation = forms.CharField(max_length=30, help_text='Optional.')
    gender = forms.CharField(max_length=30, help_text='Optional.')
    currentinstitute = forms.CharField(max_length=30, help_text='Optional.')
    year = forms.CharField(max_length=30, help_text='Optional.')
    address = forms.CharField(max_length=30, help_text='Optional.')
    avatar = forms.ImageField()
    class Meta:
        model = Employee
        fields = ('department','mobileNo','designation','gender','avatar','currentinstitute','year','address')


class Teachingform(forms.ModelForm):
    course = forms.CharField(max_length=30 , help_text='Optional.')
    start_date = forms.DateField()
    end_date = forms.DateField()

    class Meta:
        model = Teaching
        fields = ('course','start_date','end_date')

class Publicationform(forms.ModelForm):
    pub = forms.CharField(max_length=300 , help_text='Optional.')
    where = forms.CharField(max_length=300, help_text='Optional.')


    class Meta:
        model = Publication
        fields = ('pub','where')

class Educationform(forms.ModelForm):
    degree = forms.CharField(max_length=300 , help_text='Optional.')
    department = forms.CharField(max_length=300 , help_text='Optional.')
    institute = forms.CharField(max_length=300 , help_text='Optional.')
    year = forms.CharField(max_length=300, help_text='Optional.')
    country = forms.CharField(max_length=300 , help_text='Optional.')

    class Meta:
        model = Education
        fields = ('degree','department','institute','year','country')

class Projectsform(forms.ModelForm):
    title = forms.CharField(max_length=300 , help_text='Optional.')
    sponser = forms.CharField(max_length=300 , help_text='Optional.')
    duration = forms.CharField(max_length=300 , help_text='Optional.')
    role = forms.CharField(max_length=300 , help_text='Optional.')

    class Meta:
        model = Projects
        fields = ('title','sponser','duration','role')

class Achievementsform(forms.ModelForm):
    ach = forms.CharField(max_length=300 , help_text='Optional.')
    year = forms.CharField(max_length=100 , help_text='Optional.')
    details = forms.CharField(max_length=300, help_text='Optional.')


    class Meta:
        model = Achievements
        fields = ('year','ach','details')

class SearchForm(forms.Form):
    query = forms.CharField(max_length=300 , help_text='Optional.')
    class Meta:
        fields = ('query',)

class WebsiteForm(forms.Form):
    website = forms.CharField(max_length=300 , help_text='Optional.')
    class Meta:
        fields = ('website',)