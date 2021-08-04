from django.urls import path

from .views import *

urlpatterns = [
    path('', management, name='management'),
    path('admin_success/', admin_success, name='admin_success'),
    path('admin_create_appointment/', admin_create_appointment.as_view(), name='admin_create_appointment'),

    path('view_corporate/', view_corporate.as_view(), name='view_corporate'),
    path('view_appointment/', view_appointment.as_view(), name='view_appointment'),
    path('view_clients/', view_clients.as_view(), name='view_clients'),

    path('corporate_detail/<int:pk>', corporate_detail.as_view(), name='corporate_detail'),
    path('corporate_detail_edit/<int:pk>', corporate_detail_edit.as_view(), name='corporate_detail_edit'),

    path('admin_view_appointment/<int:pk>', admin_view_appointment.as_view(), name='admin_view_appointment'),
    path('admin_view_appointment_edit/<int:pk>', admin_view_appointment_edit.as_view(),
         name='admin_view_appointment_edit'),


    path('client_fill_up_onsite/<int:pk>', client_fill_up_onsite, name='client_fill_up_onsite'),

    path('admin_view_client/<int:pk>', admin_view_client.as_view(), name='admin_view_client'),
    path('clinic_view_client_edit/<int:pk>', clinic_view_client_edit.as_view(), name='clinic_view_client_edit'),

    path('lab_view_client_edit/<int:pk>', lab_view_client_edit, name='lab_view_client_edit'),
    path('lab_view_corporate_edit/<int:pk>', lab_view_corporate_edit, name='lab_view_corporate_edit'),

    path('corporate_print/<int:pk>', corporate_print.as_view(), name='corporate_print'),
    path('corporate_print_health_dec/<int:pk>', corporate_print_health_dec.as_view(), name='corporate_print_health_dec'),

    path('customers_print/<int:pk>', customers_print.as_view(), name='customers_print'),

    path('client_print/<int:pk>', client_print.as_view(), name='client_print'),
    path('client_print_health_dec/<int:pk>', client_print_health_dec.as_view(), name='client_print_health_dec'),

]
