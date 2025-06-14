from django.urls import path
from . import views


urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('success/<order_number>/',
         views.checkout_success,
         name='checkout_success'),
    path('order-history/', views.order_history, name='order_history'),
]
