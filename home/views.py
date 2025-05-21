from django.shortcuts import render

# Create your views here.

def home(request):
    """ A view for the homepage"""
    return render(request, 'home/home.html')


def about(request):
    """ A view for the about us page"""
    return render (request, 'home/about.html')