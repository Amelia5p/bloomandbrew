from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import UserProfile


@receiver(user_logged_in)
def ensure_profile_on_login(sender, request, user, **kwargs):
    UserProfile.objects.get_or_create(user=user)
