from django.contrib import admin

from clients.models import Client, lab_Client

admin.site.register(Client)
admin.site.register(lab_Client)
