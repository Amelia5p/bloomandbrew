from django.shortcuts import render, redirect
from cart.cart import Cart
from django.contrib import messages

def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, "Your cart is empty.")
        return redirect('view_cart')
    return render(request, 'checkout/checkout.html', {'cart': cart})
