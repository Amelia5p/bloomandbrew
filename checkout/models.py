import uuid
from django.db import models
from django_countries.fields import CountryField
from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=20, null=False, editable=False, unique=True)
    reference_code = models.CharField(max_length=32, null=False, editable=False, unique=True)
    
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                             null=True, blank=True, related_name='orders')
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
    total_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    cart_snapshot = models.TextField()
    stripe_pid = models.CharField(max_length=254)

    def _generate_order_number(self):
        return f"BB{uuid.uuid4().hex[:10].upper()}"

    def _generate_reference_code(self):
        return uuid.uuid4().hex.upper()

    def update_totals(self):
        self.subtotal = self.items.aggregate(models.Sum('item_total'))['item_total__sum'] or 0
        self.delivery_fee = 0 if self.subtotal >= 50 else 5
        self.total_due = self.subtotal + self.delivery_fee
        self.save()

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
        self.item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.order.order_number}"
