"""SSL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
from django.urls import re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
#from SSL/SSL/settings.py
from SSL import settings
from . import views


urlpatterns = [
    re_path(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'^a/$', views.webmail, name='webmail'),
    re_path(r'^accounts/profile/$', views.index,name='index'),
    re_path(r'^accounts/login/$', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^accounts/profile/user/$', views.edit_profile, name='user'),
    re_path(r'^accounts/profile/table/$', views.teaching, name='table'),
    re_path(r'^accounts/profile/publication/$', views.publication, name='publication'),
    re_path(r'^accounts/profile/projects/$', views.projects, name='projects'),
    re_path(r'^accounts/profile/achievements/$', views.achievements, name='achievements'),
    re_path(r'^accounts/profile/education/$', views.education, name='education'),
    re_path(r'^signup/$', views.signup, name='editprofile'),
    re_path(r'^accounts/profile/table/delete/(?P<part_id>[0-9]+)/$', views.function, name='delete_view'),
    re_path(r'^accounts/profile/publication/delete/(?P<part_id>[0-9]+)/$', views.function2, name='delete_view2'),
    re_path(r'^accounts/profile/education/delete/(?P<part_id>[0-9]+)/$', views.function3, name='delete_view3'),
    re_path(r'^accounts/profile/projects/delete/(?P<part_id>[0-9]+)/$', views.function4, name='delete_view4'),
    re_path(r'^accounts/profile/achievements/delete/(?P<part_id>[0-9]+)/$', views.function5, name='delete_view5'),

    re_path(r'^profile/(?P<username>.+)/$', views.show_main, name='show'),
    re_path(r'^search/$', views.find_user_by_name, name='search1'),
    re_path(r'^password_reset/$', auth_views.PasswordResetForm, name='password_reset'),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)