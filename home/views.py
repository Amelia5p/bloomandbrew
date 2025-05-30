from django.shortcuts import render

# Create your views here.

def home(request):
    """ A view for the homepage"""
    return render(request, 'home/home.html')


def about(request):
    """ A view for the about us page"""
    return render (request, 'home/about.html')

from products.models import Product

from django.shortcuts import render
from products.models import Product

def home(request):
    """ Show homepage with featured products and bundle of the week """
    featured_products = Product.objects.filter(is_featured=True)[:4]
    bundle_of_the_week = Product.objects.filter(bundle_of_the_week=True).first()

    return render(request, 'home/home.html', {
        'featured_products': featured_products,
        'bundle_of_the_week': bundle_of_the_week,
    })

