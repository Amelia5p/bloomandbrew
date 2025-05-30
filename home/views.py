from django.shortcuts import render

# Create your views here.

def home(request):
    """ A view for the homepage"""
    return render(request, 'home/home.html')


def about(request):
    """ A view for the about us page"""
    return render (request, 'home/about.html')

from products.models import Product

def home(request):
    """ Show featured products on homepage """
    featured_products = Product.objects.filter(is_featured=True)[:4]  # Limit to 4
    return render(request, 'home/home.html', {
        'featured_products': featured_products
    })
