
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    """Display a list of all products."""
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, slug):
    """Display detailed view of a single product."""
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})