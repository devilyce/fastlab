import uuid

from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

from cal.models import setDay, setTime
from locations.models import TestLocation
from products.models import Product


class Customers(models.Model):
    date_added = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    number_of_person = models.IntegerField(null=True, blank=True)
    test_location = models.ForeignKey(TestLocation, on_delete=models.SET_NULL, null=True)
    booking_date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    contact_number = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    civil_status = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(max_length=300, null=True, blank=True)
    senior_pwd_id = models.CharField(max_length=50, null=True, blank=True)
    senior_pwd_file = models.FileField(null=True, blank=True, upload_to="senior_pwd_file/")
    reference_number = models.CharField(max_length=50, null=True, blank=True, unique=True)

    PAYMENT = [
        ('PENDING', 'Pending'),
        ('VERIFIED', 'Verified'),
    ]
    PAYMENT_METHOD = [
        ('', ''),
        ('CASH', 'Cash'),
        ('BANK', 'Bank'),
        ('GCASH', 'GCash'),
        ('PAYPAL', 'Paypal'),

    ]
    payment_status = models.CharField(max_length=20, choices=PAYMENT, default='PENDING')
    refund_discount = models.IntegerField(null=True, blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='', null=True, blank=True)
    payment_reference = models.CharField(max_length=20, null=True, blank=True)
    count = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.first_name + '' + self.last_name

    class Meta:
        unique_together = ('email', 'reference_number')

    def save(self, *args, **kwargs):
        if self.reference_number is None:
            self.reference_number = str(uuid.uuid4())[:11].replace('-', '').lower()
        return super().save(*args, **kwargs)

    @property
    def get_total(self):
        total = self.product.price * int(self.number_of_person)
        return total

    @property
    def get_discount(self):
        if self.refund_discount is not None and self.senior_pwd_id is not None:
            discount = self.refund_discount + (0.2 * float(self.get_total))
        elif self.senior_pwd_id is not None:
            discount = 0.2 * float(self.get_total)
        elif self.refund_discount is not None:
            discount = self.refund_discount
        else:
            discount = None
        return discount

    @property
    def get_total_price_after_discount(self):
        if self.refund_discount is not None:
            total_price = self.get_total - int(self.refund_discount)
        elif self.senior_pwd_id is not None:
            total_price = float(self.get_total) - self.get_discount
        else:
            total_price = self.get_total
        return total_price

    def get_absolute_url(self):
        return reverse('admin_view_appointment', kwargs={'pk': self.pk})

@receiver(post_save, sender=Customers)
def send_email_customer(sender, instance, created, **kwargs):
    if created:
        subject = 'Thanks'
        message = render_to_string('customers/email/mail_confirmation.html', {
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'middle_name': instance.middle_name,
            'email': instance.email,
            'test_location': instance.test_location,
            'booking_date': instance.booking_date,
            'time': instance.time,
            'product': instance.product,
            'get_total': instance.get_total,
            'get_discount': instance.get_discount,
            'get_total_price_after_discount': instance.get_total_price_after_discount,
            'reference_number': instance.reference_number,
            'url': reverse('health_declaration', kwargs={'pk': instance.pk}),
        })

        recipient = instance.email
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)

        obj_day = instance.booking_date
        obj_day = str(obj_day)
        obj_day = setDay.objects.get(date=obj_day)
        obj_day.count += 1
        obj_day.save()

        obj_time = instance.time
        obj_time = str(obj_time)
        obj_time = setTime.objects.get(name=obj_time, date=instance.booking_date)
        obj_time.count += 1
        obj_time.save()
