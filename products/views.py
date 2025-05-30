
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from django.db.models import Q
from django.contrib import messages
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required



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
    """ Displays a single product's details """
    product = get_object_or_404(Product, slug=slug)
    all_reviews = product.reviews.all()
    show_all = request.GET.get('all') == '1'
    reviews = all_reviews if show_all else all_reviews[:3]

    return render(request, 'products/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'show_all_reviews': show_all,
        'review_count': all_reviews.count(),
    })


def shop_brews(request):
    """ Brews-only product page """
    products = Product.objects.filter(category='coffee')
    return render(request, 'products/shop_brews.html', {'products': products})


def shop_blooms(request):
    """ Blooms-only product page """
    products = Product.objects.filter(category='bouquet')
    return render(request, 'products/shop_blooms.html', {'products': products})

def shop_bundles(request):
    """ Bundles-only product page """
    products = Product.objects.filter(category='bundle')
    return render(request, 'products/shop_bundles.html', {'products': products})


def add_review(request, product_slug):
    """ Add review page """
    product = get_object_or_404(Product, slug=product_slug)

    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to leave a review.")
        return redirect('account_login')

    existing_review = Review.objects.filter(product=product, user=request.user).first()
    if existing_review:
        messages.warning(request, "You've already reviewed this product.")
        return redirect('product_detail', slug=product.slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "Thanks for your review!")
            return redirect('product_detail', slug=product.slug)
    else:
        form = ReviewForm()

    return render(request, 'products/add_review.html', {'form': form, 'product': product})



@login_required
def edit_review(request, product_slug, review_id):
    """ Edit review page """
    product = get_object_or_404(Product, slug=product_slug)
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated.")
            return redirect('product_detail', slug=product.slug)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'products/edit_review.html', {'form': form, 'product': product})


@login_required
def delete_review(request, product_slug, review_id):
    """ Delete review"""
    product = get_object_or_404(Product, slug=product_slug)
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        review.delete()
        messages.success(request, "Your review has been deleted.")
        return redirect('product_detail', slug=product.slug)

    return render(request, 'products/delete_review.html', {'review': review, 'product': product})

