from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from sslproject.models import Employee


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class SignUpForm2(forms.ModelForm):
    department=forms.CharField(max_length=30, required=False)

    class Meta:
        model = Employee
        fields=('department',)

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
    avatar = forms.ImageField()
    class Meta:
        model = Employee
        fields = ('department','avatar')
