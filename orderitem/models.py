from django.db import models
from django.urls import reverse

from locations.models import TestLocation
from products.models import Product


class OrderItem(models.Model):
    date_added = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    number_of_person = models.CharField(max_length=50)
    test_location = models.ForeignKey(TestLocation, on_delete=models.SET_NULL, null=True)
    day = models.DateField()
    month = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    civil_status = models.CharField(max_length=20)
    date_of_birth = models.DateField(max_length=20)
    gender = models.CharField(max_length=20)
    address = models.TextField(max_length=300)
    senior_pwd_id = models.CharField(max_length=50, null=True, blank=True)
    senior_pwd_file = models.FileField(null=True, blank=True, upload_to="senior_pwd_file/")

    def __str__(self):
        return self.first_name + '' + self.last_name

    @property
    def get_total(self):
        total = self.product.price * int(self.number_of_person)
        return total

    @property
    def get_discount(self):
        if self.senior_pwd_id is not None:
            discount = 0.2 * float(self.get_total)
        else:
            discount = None
        return discount

    @property
    def get_total_price_after_discount(self):
        return float(self.get_total) - self.get_discount

    def get_absolute_url(self):
        return reverse('confirm_appointment', kwargs={'pk': self.pk})
