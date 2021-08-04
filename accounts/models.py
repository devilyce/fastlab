from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    date_added = models.DateField(auto_now_add=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
