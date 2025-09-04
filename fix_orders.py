from decimal import Decimal
from django.db import transaction
from checkout.models import Order
print(">>> Starting order fix script")

TARGETS = ["BB456A064ED8", "BB028ACEE66D"]

def unit_price(product):
    if product.special_offer_price and product.special_offer_price < product.price:
        return product.special_offer_price
    return product.price

for order_number in TARGETS:
    try:
        order = Order.objects.get(order_number=order_number)
    except Order.DoesNotExist:
        print(f"Order not found: {order_number}")
        continue

    print(f"\n--- {order.order_number} BEFORE ---")
    print("Subtotal:", order.subtotal,
          "Delivery:", order.delivery_fee,
          "Discount:", order.discount_amount,
          "Total:", order.total_due)

    with transaction.atomic():
        for item in order.items.select_related("product"):
            expected = (unit_price(item.product) * item.quantity).quantize(Decimal("0.01"))
            if item.item_total != expected:
                item.item_total = expected
                item.save(update_fields=["item_total"])
        order.update_totals(persist=True)

    print(f"--- {order.order_number} AFTER ---")
    print("Subtotal:", order.subtotal,
          "Delivery:", order.delivery_fee,
          "Discount:", order.discount_amount,
          "Total:", order.total_due)

    if order.items.count() == 0:
        print("Note: this order has no items. Likely a test/abandoned record.")
    elif order.total_due == Decimal("0.00"):
        print("Note: total is still 0.00. Check for full discount or zero-priced items.")
