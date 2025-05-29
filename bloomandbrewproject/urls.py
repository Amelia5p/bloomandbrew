from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from checkout.webhooks import stripe_webhook


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('checkout/wh', stripe_webhook, name='stripe_webhook'),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('profile/', include('profiles.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'bloomandbrewproject.views.custom_404'
handler500 = 'bloomandbrewproject.views.custom_500'