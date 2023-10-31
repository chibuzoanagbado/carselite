from django.shortcuts import render
from .models import Team

# Create your views here.

def home(requests):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(requests, 'pages/home.html', data)

def about(requests):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(requests, 'pages/about.html', data)

def services(requests):
    return render(requests, 'pages/services.html')

def contact(requests):
    return render(requests, 'pages/contact.html')
