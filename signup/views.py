from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


@login_required
def home(request):
    return render(request, 'signup/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            if User.objects.filter(username = request.POST['username']).exists():
                information = "Username already taken."
            elif len(form.cleaned_data.get('password1'))<8:
                information = "Password must be atleast 8 characters long."
            elif form.cleaned_data.get('password1')!= form.cleaned_data.get('password2'):
                information = "Passwords didn`t match."
            else:
                information = "Password too weak: Cannot be numeric only."
            return render(request ,"signup/signup.html",
                                      {
                                          'form':form,
                                          'invalid': True,
                                          'information': information,
                                      }
                          )
    else:
        form = UserCreationForm()
    return render(request, 'signup/signup.html', {'form': form})

