import re
from django.contrib.auth.models import User
def func(request):
    str = open('sslproject/Crawler/file.text', 'r')
    for line in str:
        s=" ".join(re.findall(r'"([^"]*)"', line))
        if s:
            user = User.objects.get(username=request.user)
            user.employee.designation = s
            user.employee.save()
            user.save()