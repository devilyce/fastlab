from django.db import models
from django.urls import reverse


class PersonManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(disable=True)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    disable = models.BooleanField(default=False)

    objects = PersonManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('create_appointment', kwargs={'pk': self.pk})
