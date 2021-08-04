from django.contrib import admin

from cal.models import setYear, setMonth, setDay, setTime, timeChoice

admin.site.register(setYear)
admin.site.register(setMonth)
admin.site.register(setDay)
admin.site.register(setTime)
admin.site.register(timeChoice)
