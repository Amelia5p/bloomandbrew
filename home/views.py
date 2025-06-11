from django.shortcuts import render, redirect
from products.models import Product
import requests
from django.conf import settings
from django.contrib import messages


def about(request):
    """A view for the about us page."""
    return render(request, 'home/about.html')


def home(request):
    """Show homepage with featured products and bundle of the week."""
    featured_products = Product.objects.filter(is_featured=True)[:4]
    bundle_of_the_week = (
        Product.objects
        .filter(bundle_of_the_week=True)
        .first()
    )

    return render(
        request,
        'home/home.html',
        {
            'featured_products': featured_products,
            'bundle_of_the_week': bundle_of_the_week,
        },
    )


def newsletter_signup(request):
    """Sign up user email to Mailchimp newsletter."""
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            messages.error(request, "Please enter a valid email.")
            return redirect(request.META.get('HTTP_REFERER', 'home'))

        url = (
            f"https://{settings.MAILCHIMP_DATA_CENTER}"
            f".api.mailchimp.com/3.0/lists/"
            f"{settings.MAILCHIMP_AUDIENCE_ID}/members"
        )
        payload = {
            'email_address': email,
            'status': 'subscribed',
        }

        try:
            response = requests.post(
                url,
                auth=('anystring', settings.MAILCHIMP_API_KEY),
                json=payload,
                timeout=10,
            )
            if response.status_code in (200, 204):
                messages.success(request, "Thanks for subscribing!")
            elif response.status_code == 400:
                error_detail = response.json().get('detail', '')
                if 'is already a list member' in error_detail:
                    messages.info(request, "You're already subscribed.")
                else:
                    messages.error(
                        request,
                        f"Mailchimp error: {error_detail}",
                    )
            else:
                messages.error(
                    request,
                    f"Unexpected error: {response.status_code}",
                )
        except requests.exceptions.RequestException as e:
            print("Mailchimp connection error:", e)
            messages.error(
                request,
                "Could not connect to the mailing list service."
                " Please try again later.",
            )

    return redirect(request.META.get('HTTP_REFERER', 'home'))
