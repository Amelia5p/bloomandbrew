from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('newsletter-signup/', views.newsletter_signup, name='newsletter_signup'),
  ]