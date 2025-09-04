# checkout/models.py
import uuid
from decimal import Decimal, ROUND_HALF_UP
from django.db import models
from django_countries.fields import CountryField
from products.models import Product
from profiles.models import UserProfile


from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class PromoCode(models.Model):
    code = models.CharField(max_length=40, unique=True)
    percent_off = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Enter percent discount as a number, e.g. 10 = 10%."
    )
    is_active = models.BooleanField(default=True)

    def clean(self):
        if self.percent_off is not None and self.percent_off <= 0:
            raise ValidationError({"percent_off": "Promo code must be greater than 0%."})

    def __str__(self):
        return f"{self.code} ({self.percent_off}% off)"



class Order(models.Model):
    order_number = models.CharField(max_length=20, null=False, editable=False, unique=True)
    reference_code = models.CharField(max_length=32, null=False, editable=False, unique=True)

    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=75)
    email_address = models.EmailField()
    contact_number = models.CharField(max_length=20)

    address_line_1 = models.CharField(max_length=80)
    address_line_2 = models.CharField(max_length=80, blank=True)
    town = models.CharField(max_length=50)
    county = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = CountryField()

    created_on = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0)

 
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    applied_promo = models.ForeignKey(PromoCode, null=True, blank=True, on_delete=models.SET_NULL)

    total_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    cart_snapshot = models.TextField()
    stripe_pid = models.CharField(max_length=254)

    FREE_DELIVERY_THRESHOLD = Decimal("50.00")
    DELIVERY_FLAT = Decimal("5.00")

    def _generate_order_number(self):
        return f"BB{uuid.uuid4().hex[:10].upper()}"

    def _generate_reference_code(self):
        return uuid.uuid4().hex.upper()

    def _calc_delivery(self) -> Decimal:
        return Decimal("0.00") if self.subtotal >= self.FREE_DELIVERY_THRESHOLD else self.DELIVERY_FLAT

    def update_totals(self, persist: bool = True):
        from django.db.models import Sum
        sum_items = self.items.aggregate(s=Sum('item_total'))['s'] or Decimal("0.00")
        self.subtotal = sum_items.quantize(Decimal("0.01"))

        self.delivery_fee = self._calc_delivery()

        
        if self.applied_promo and self.applied_promo.is_active:
            self.discount_amount = (
                self.subtotal * (self.applied_promo.percent_off / Decimal("100"))
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        else:
            self.discount_amount = Decimal("0.00")

        total = self.subtotal + self.delivery_fee - self.discount_amount
        self.total_due = max(total, Decimal("0.00")).quantize(Decimal("0.01"))

        if persist:
            self.save(update_fields=['subtotal', 'delivery_fee', 'discount_amount', 'total_due'])

    def apply_promo_code(self, code_str: str) -> bool:
        """Try applying a promo code by string."""
        try:
            promo = PromoCode.objects.get(code__iexact=code_str.strip(), is_active=True)
        except PromoCode.DoesNotExist:
            return False
        self.applied_promo = promo
        self.update_totals(persist=True)
        return True

    def clear_promo(self):
        self.applied_promo = None
        self.discount_amount = Decimal("0.00")
        self.update_totals(persist=True)

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        if not self.reference_code:
            self.reference_code = self._generate_reference_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=6, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        price = self.product.special_offer_price if getattr(self.product, "has_discount", False) and self.product.special_offer_price else self.product.price
        self.item_total = price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.order.order_number}"
