from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .models import Profile


def accounts_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
        )

post_save.connect(accounts_profile, sender=User)
