from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = (
            'order_number',
            'reference_code',
            'user',
            'subtotal',
            'delivery_fee',
            'total_due',
            'stripe_pid',
            'cart_snapshot',
            'created_on')
