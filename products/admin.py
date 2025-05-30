from django.contrib import admin
from .models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
    )
    ordering = ('sku',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'comment', 'created_on')
    list_filter = ('rating', 'product', 'created_on')
    search_fields = ('user__username', 'product__name', 'comment')
    ordering = ('-rating', '-created_on')


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
