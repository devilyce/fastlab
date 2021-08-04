from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('book_now', book_now.as_view(), name='book_now'),
    path('create_appointment/<int:pk>', create_appointment.as_view(), name="create_appointment"),
    path('confirm_appointment/<int:pk>', confirm_appointment, name="confirm_appointment"),
    path('mail_sent/', mail_sent, name="mail_sent"),
    path('success/', success, name="success"),
    path('error/', error, name="error"),
    path('health_declaration/<int:pk>', health_declaration, name="health_declaration"),
    path('create_appointment/year-json/', get_json_year_data, name='year-json'),
    path('create_appointment/month-json/<str:year>/', get_json_month_data, name='month-json'),
    path('create_appointment/day-json/<str:month>/', get_json_day_data, name='day-json'),
    path('create_appointment/time-json/<str:day>/', get_json_time_data, name='time-json'),
]
