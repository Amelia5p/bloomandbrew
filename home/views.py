from django.shortcuts import render

# Create your views here.

def home(request):
    """ A view for the homepage"""
    return render(request, 'home/home.html')

