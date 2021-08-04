# from django.conf.global_settings import EMAIL_BACKEND
# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.template.loader import render_to_string
#
# from customers.models import Customers
#
#
# @receiver(post_save, sender=Customers)
# def send_email_customer(sender, instance, created, **kwargs):
#     subject = 'Thanks'
#     message = render_to_string('customers/email/mail_confirmation.html', {
#         'first_name': instance.first_name,
#         'last_name': instance.last_name,
#         'middle_name': instance.middle_name,
#         'email': instance.email,
#         'test_location': instance.test_location,
#         'set_date': instance.set_date,
#         'set_time': instance.set_time,
#         'product': instance.product,
#         'price': instance.price,
#         'get_total': instance.get_total,
#         'reference_number': instance.reference_number,
#     })
#     recepient = instance.email
#
#     send_mail(subject, message, EMAIL_BACKEND, [recepient], fail_silently=False)
#
#
# post_save.connect(send_email_customer, sender=Customers)