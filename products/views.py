
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q



def product_list(request):
    """ Display list of products, filter, sort"""
    query = request.GET.get('q')
    category = request.GET.get('category')
    sort = request.GET.get('sort')

    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )

    if category:
        products = products.filter(category=category)

    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'name_asc':
        products = products.order_by('name')
    elif sort == 'name_desc':
        products = products.order_by('-name')

    return render(request, 'products/product_list.html', {
        'products': products,
        'search_query': query,
    })

def product_detail(request, slug):
    """Display detailed view of a single product."""
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})

def shop_brews(request):
    """ Brews-only product page """
    products = Product.objects.filter(category='coffee')
    return render(request, 'products/shop_brews.html', {'products': products})

def shop_blooms(request):
    """ Blooms-only product page """
    products = Product.objects.filter(category='bouquet')
    return render(request, 'products/shop_blooms.html', {'products': products})
