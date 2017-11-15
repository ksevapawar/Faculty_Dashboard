from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from sslproject.models import Employee, Teaching, Publication, Education, Achievements, Projects


class PublicationInline(admin.StackedInline):
    model = Publication
    can_delete = False
    verbose_name_plural = 'publication'

class AchievementsInline(admin.StackedInline):
       model = Achievements
       can_delete = False
       verbose_name_plural = 'achievements'


class ProjectsInline(admin.StackedInline):
    model = Projects
    can_delete = False
    verbose_name_plural = 'projects'


class EducationInline(admin.StackedInline):
    model = Education
    can_delete = False
    verbose_name_plural = 'education'

class TeachingInline(admin.StackedInline):
    model = Teaching
    can_delete = False
    verbose_name_plural = 'teaching'
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline, TeachingInline , EducationInline ,PublicationInline ,AchievementsInline,ProjectsInline)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Teaching)
admin.site.register(Publication)
admin.site.register(Education)
admin.site.register(Achievements)
admin.site.register(Projects    )