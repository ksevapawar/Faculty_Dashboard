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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from SSL import settings
from . import views


urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^accounts/profile/$', views.index,name='index'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/profile/user/$', views.edit_profile, name='user'),
    url(r'^accounts/profile/table/$', views.teaching, name='table'),
    url(r'^accounts/profile/publication/$', views.publication, name='publication'),
    url(r'^signup/$', views.signup, name='editprofile'),
    url(r'^accounts/profile/table/delete/(?P<part_id>[0-9]+)/$', views.function, name='delete_view'),
    url(r'^accounts/profile/publication/delete/(?P<part_id>[0-9]+)/$', views.function2, name='delete_view2'),
    url(r'^accounts/profile/education/delete/(?P<part_id>[0-9]+)/$', views.function3, name='delete_view3'),
    url(r'^accounts/profile/education/$', views.education, name='education'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)