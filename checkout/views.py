from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, OrderItem
from .forms import OrderForm
from cart.cart import Cart
from products.models import Product




def checkout(request):
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, "Your cart is empty.")
        return redirect('view_cart')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user.userprofile if request.user.is_authenticated else None
            order.cart_snapshot = str(cart)
            order.stripe_pid = 'TEMP-PLACEHOLDER'
            order.save()

            for item in cart:
                product = item['product']
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item['quantity'],
                )

            order.update_totals()
            cart.clear()

            messages.success(request, f"Order {order.order_number} placed successfully!")
            return redirect('checkout_success', order_number=order.order_number)
        else:
            messages.error(request, "There was an error with your form. Please review and try again.")
    else:
        form = OrderForm()

    return render(request, 'checkout/checkout.html', {
        'form': form,
        'cart': cart,
    })


def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, 'checkout/checkout_success.html', {'order': order})
