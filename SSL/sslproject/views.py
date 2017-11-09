

from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from SSL import settings
from sslproject.models import Employee
from sslproject.forms import SignUpForm, EditProfileForm, EditProfileForm2, SignUpForm2
# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from sslproject.tokens import account_activation_token


@login_required(login_url='/login')
def index(request):
    return render(request, 'dashboard/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user':user, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # Sending activation link in terminal
            # user.email_user(subject, message)

            #to_list = [save_it.email, settings.EMAIL_HOST_USER]

            mail_subject = 'Activate your blog account.'
            from_mail=settings.EMAIL_HOST_USER
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration.')
            #return render(request, 'acc_active_sent.html')
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
        form2 = EditProfileForm2(request.POST, instance=request.user.employee)
        if form.is_valid():
            form.save()
        if form2.is_valid():
            form2.save()
        return redirect('/accounts/profile/user')

    else:

        return render(request, 'dashboard/user.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')