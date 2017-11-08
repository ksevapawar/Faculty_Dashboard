from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='employee')
    department = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "User Profiles"

    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
