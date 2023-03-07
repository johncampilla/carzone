from django.shortcuts import render
from .models import *
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured = True).order_by('-created_date')
    
    context = { 
        'teams' : teams,
        'featured_cars': featured_cars,
    }
    return render(request, 'pages/home.html', context)


def about(request):
    teams = Team.objects.all()
    context = { 
        'teams' : teams,
    }
    return render(request, 'pages/about.html', context)

def services(request):
    return render(request, 'pages/services.html')

def contacts(request):
    return render(request, 'pages/contacts.html')