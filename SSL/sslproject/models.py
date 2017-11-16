import datetime
from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    department = models.CharField(max_length=100)
    mobileNo = models.CharField(max_length=100,default=' ')
    designation = models.CharField(max_length=100, default=' ')
    gender = models.CharField(max_length=100, default=' ')
    currentinstitute = models.CharField(max_length=100, default=' ')
    year = models.CharField(max_length=100, default=' ')
    address = models.CharField(max_length=100, default=' ')

    avatar = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

    class Meta:
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)

class Teaching(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='teaching')
    course = models.CharField(max_length=100)
    start_date =  models.CharField(max_length=100,default=' ')
    end_date = models.CharField(max_length=100,default=' ')

    def __str__(self):
        return self.user.username

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publication')
    pub = models.CharField(max_length=300)
    where = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=300)
    sponser = models.CharField(max_length=300)
    duration = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username




class Achievements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    ach = models.CharField(max_length=300)
    year =  models.CharField(max_length=100)
    details = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username

post_save.connect(create_user_profile, sender=User)