from django.urls import path
from . import views
from .webhooks import stripe_webhook


urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('success/<order_number>/', views.checkout_success, name='checkout_success'),
    path('order-history/', views.order_history, name='order_history'),
    path('checkout/wh', stripe_webhook, name='stripe_webhook'),
]

