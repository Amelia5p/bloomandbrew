from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('blooms/', views.shop_blooms, name='shop_blooms'),
    path('brews/', views.shop_brews, name='shop_brews'),
    path('bundles/', views.shop_bundles, name='shop_bundles'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('product/<slug:product_slug>/review/',
         views.add_review, name='add_review'),
    path('product/<slug:product_slug>/review/<int:review_id>/edit/',
         views.edit_review, name='edit_review'),
    path('product/<slug:product_slug>/review/<int:review_id>/delete/',
         views.delete_review, name='delete_review'),
    path('admin/products/', views.manage_products, name='product_admin'),
    path('admin/products/add/', views.add_product, name='add_product'),
    path('admin/products/<int:product_id>/edit/',
         views.edit_product, name='edit_product'),
    path('admin/products/<int:product_id>/delete/',
         views.delete_product, name='delete_product'),
    ]
