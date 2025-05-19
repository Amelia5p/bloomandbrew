from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('blooms/', views.shop_blooms, name='shop_blooms'),
    path('brews/', views.shop_brews, name='shop_brews'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),

]
