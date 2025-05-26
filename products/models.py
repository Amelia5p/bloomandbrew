from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

class Product(models.Model):
    """
Product model representing items sold in the store.

Includes category, pricing (with optional discount), image, stock, and auto-generated slug.
    """

    CATEGORY_CHOICES = [
        ('bouquet', 'Bouquet'),
        ('coffee', 'Coffee'),
        ('bundle', 'Bundle'),
    ]

    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    special_offer_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = CloudinaryField('image')
    stock = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def has_discount(self):
        return self.special_offer_price is not None and self.special_offer_price < self.price

    def display_price(self):
        return self.special_offer_price if self.has_discount() else self.price

    def __str__(self):
        return self.name
