from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    Stores customer preferences and shipping info
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    address_1 = models.CharField(
        "Address Line 1",
        max_length=80,
        blank=True,
        null=True
    )
    address_2 = models.CharField(
        "Address Line 2",
        max_length=80,
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=40,
        blank=True,
        null=True
    )
    county = models.CharField(
        max_length=80,
        blank=True,
        null=True
    )
    country = CountryField(
        blank_label='Country',
        blank=True,
        null=True
    )
    postcode = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    def __str__(self):
        return (
            self.user.get_full_name()
            or self.user.username
        )


@receiver(post_save, sender=User)
def create_or_update_user_profile(
    sender, instance, created, **kwargs
):
    """
    Creates or updates the UserProfile automatically
    whenever a User is saved.
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
