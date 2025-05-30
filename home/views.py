from django.shortcuts import render, redirect
from products.models import Product
import requests
from django.conf import settings
from django.contrib import messages


def home(request):
    """ A view for the homepage"""
    return render(request, 'home/home.html')


def about(request):
    """ A view for the about us page"""
    return render (request, 'home/about.html')



def home(request):
    """ Show homepage with featured products and bundle of the week """
    featured_products = Product.objects.filter(is_featured=True)[:4]
    bundle_of_the_week = Product.objects.filter(bundle_of_the_week=True).first()

    return render(request, 'home/home.html', {
        'featured_products': featured_products,
        'bundle_of_the_week': bundle_of_the_week,
    })


# Mailchimp newsletter view
def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            messages.error(request, "Please enter a valid email.")
            return redirect('home')

       
        url = f"https://{settings.MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0/lists/{settings.MAILCHIMP_AUDIENCE_ID}/members"

        payload = {
            "email_address": email,
            "status": "subscribed"
        }

        
        response = requests.post(
            url,
            auth=("anystring", settings.MAILCHIMP_API_KEY),
            json=payload
        )

        
        if response.status_code in [200, 204]:
            messages.success(request, "Thanks for subscribing!")
        elif response.status_code == 400 and 'already' in response.text:
            messages.info(request, "You're already subscribed.")
        else:
            messages.error(request, "Something went wrong. Please try again.")

    return redirect('home')
