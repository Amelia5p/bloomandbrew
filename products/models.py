from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Product model representing items sold in the store.

    Includes category, pricing (with optional discount), image, stock,
    and auto-generated slug.
    """

    CATEGORY_CHOICES = [
        ("bouquet", "Bouquet"),
        ("coffee", "Coffee"),
        ("bundle", "Bundle"),
    ]

    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    special_offer_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    image = CloudinaryField("image")
    stock = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)
    is_featured = models.BooleanField(default=False)
    bundle_of_the_week = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def has_discount(self):
        return (
            self.special_offer_price is not None
            and self.special_offer_price < self.price
        )

    def display_price(self):
        return self.special_offer_price if self.has_discount() else self.price

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Stores a user review for a product, including star
    rating and optional comment.
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)]
    )
    comment = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
        unique_together = ("product", "user")

    def __str__(self):
        return f"{self.product.name} - {self.user.username} ({self.rating}★)"


class Wishlist(models.Model):
    """
    A wishlist belonging to a user. One per user.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="wishlist",
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"


class WishlistItem(models.Model):
    """
    Individual product saved to a user's wishlist.
    """

    wishlist = models.ForeignKey(
        Wishlist, on_delete=models.CASCADE, related_name="items"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="wishlisted_in"
    )
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("wishlist", "product")
        ordering = ["-added_on"]

    def __str__(self):
        return (
            f"{self.product.name} in "
            f"{self.order.order_number}"
        )
