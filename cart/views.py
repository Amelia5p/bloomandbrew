from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .cart import Cart
from django.contrib import messages



def add_to_cart(request, product_id):
    """Add a product to the cart or update its quantity."""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    override = request.POST.get('override_quantity') == 'true'
    cart.add(product=product, quantity=quantity, override_quantity=override)
    messages.success(request, f'{"Updated" if override else "Added"} {quantity} × "{product.name}" to your cart.')
    return redirect('product_list')


def remove_from_cart(request, product_id):
    """Remove a product from the cart."""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'Removed "{product.name}" from your cart.')
    return redirect('view_cart')


def view_cart(request):
    """Display the full cart contents."""
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})
