from django.shortcuts import render
from django.conf import settings


def index(request):
    """A view to return the index page"""
    return render(request, 'home/index.html')


def home_about(request):
    context = {
        'api_key': settings.GOOGLE_MAPS_API_KEY
    }
    """A view to return the home_about page"""
    return render(request, 'home/home_about.html', context)
