import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Order, OrderItem
from .forms import OrderForm
from cart.cart import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY


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
            order.stripe_pid = request.POST.get('stripe_pid')
            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                )

            order.update_totals()
            cart.clear()
            messages.success(request, f"Order {order.order_number} placed successfully!")
            return redirect('checkout_success', order_number=order.order_number)
        else:
            messages.error(request, "There was an error with your form.")
    else:
        if request.user.is_authenticated:
            profile = request.user.userprofile
            initial_data = {
                'full_name': request.user.get_full_name(),
                'email_address': request.user.email,
                'contact_number': profile.phone,
                'address_line_1': profile.address_1,
                'address_line_2': profile.address_2,
                'town': profile.city,
                'county': profile.county,
                'postal_code': profile.postcode,
                'country': profile.country,
            }
            form = OrderForm(initial=initial_data)
        else:
            form = OrderForm()

        total = cart.get_total_price()
        if total == 0:
            messages.error(request, "Your cart total is €0. Please add items before checking out.")
            return redirect('view_cart')

        total_cents = int(total * 100)
        intent = stripe.PaymentIntent.create(
            amount=total_cents,
            currency='eur',
        )

    context = {
        'form': form,
        'cart': cart,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
        'stripe_pid': intent.id,
        'total_due': total,
    }
    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, 'checkout/checkout_success.html', {'order': order})


@login_required
def order_history(request):
    user_profile = request.user.userprofile
    orders = Order.objects.filter(user=user_profile).order_by('-created_on')

    return render(request, 'checkout/order_history.html', {
        'orders': orders
    })
