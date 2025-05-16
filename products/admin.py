from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
    )
    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
