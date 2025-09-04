from decimal import Decimal
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import OrderItem

@receiver(pre_save, sender=OrderItem)
def set_item_total(sender, instance: OrderItem, **kwargs):
    """
    Always compute item_total from the product price before saving.
    """
    p = instance.product
    price = p.special_offer_price if (p.special_offer_price and p.special_offer_price < p.price) else p.price
    instance.item_total = (price * instance.quantity).quantize(Decimal("0.01"))

@receiver(post_save, sender=OrderItem)
def recalc_order_totals_on_save(sender, instance: OrderItem, **kwargs):
    instance.order.update_totals()

@receiver(post_delete, sender=OrderItem)
def recalc_order_totals_on_delete(sender, instance: OrderItem, **kwargs):
    instance.order.update_totals()
