from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product', 'quantity', 'item_total')
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'full_name',
        'email_address',
        'created_on',
        'total_due',
        'stripe_pid',
    )
    list_filter = ('created_on', 'country', 'total_due')
    search_fields = (
        'order_number',
        'full_name',
        'email_address',
        'stripe_pid')

    readonly_fields = (
        'order_number',
        'reference_code',
        'created_on',
        'subtotal',
        'delivery_fee',
        'total_due',
        'cart_snapshot',
        'stripe_pid',
    )

    inlines = [OrderItemInline]

    fieldsets = (
        ('Order Info', {
            'fields': (
                'order_number', 'reference_code', 'created_on', 'stripe_pid'
            )
        }),
        ('Customer Details', {
            'fields': (
                'user', 'full_name', 'email_address', 'contact_number',
            )
        }),
        ('Delivery Address', {
            'fields': (
                'address_line_1', 'address_line_2',
                'town', 'county', 'postal_code', 'country',
            )
        }),
        ('Financials', {
            'fields': (
                'subtotal', 'delivery_fee', 'total_due', 'cart_snapshot',
            )
        }),
    )

    ordering = ('-created_on',)
