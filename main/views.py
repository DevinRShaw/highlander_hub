from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "main/index.html",{})


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponse("User created successfully!")
        else:
            #form = UserCreationForm() caused error 
            return render(request, 'main/register.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'main/register.html', {'form': form})


