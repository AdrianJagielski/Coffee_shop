'''
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def login(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(username=username, password=password)

        form = AuthenticationForm(request.POST)
        if (not user):
            return render(request ,"registration/login.html",{'form':form,'invalid': True })
        else:
            return render(request, "signup/home.html",)'''