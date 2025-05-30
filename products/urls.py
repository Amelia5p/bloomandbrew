from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('blooms/', views.shop_blooms, name='shop_blooms'),
    path('brews/', views.shop_brews, name='shop_brews'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('product/<slug:product_slug>/review/', views.add_review, name='add_review'),
    path('product/<slug:product_slug>/review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('product/<slug:product_slug>/review/<int:review_id>/delete/', views.delete_review, name='delete_review'),

]
