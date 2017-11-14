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

    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)

class Teaching(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='teaching')
    course = models.CharField(max_length=100)
    start_date =  models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)


post_save.connect(create_user_profile, sender=User)
