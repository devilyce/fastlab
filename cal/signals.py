import datetime
from calendar import monthrange

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import setMonth, setDay, setTime


@receiver(post_save, sender=setMonth)
def create_days(sender, instance, created, **kwargs):
    if created:
        month = instance
        date = instance.date
        yr = instance.date.year
        m = instance.date.month
        mr = monthrange(yr, m)[1]

        day_delta = datetime.timedelta(days=1)

        start_date = date
        end_date = start_date + mr * day_delta
        day = 0

        for i in range((end_date - start_date).days):
            date = start_date + i * day_delta
            day += 1
            setDay.objects.create(name=day, month=month, date=date, count=0)


@receiver(post_save, sender=setDay)
def create_time(sender, instance, created, **kwargs):
    if created:
        instance = instance
        date = instance.date

        start_time = datetime.timedelta(hours=9)
        count = 0
        while count < 15:
            count += 1
            start_time = start_time + datetime.timedelta(minutes=30)

            time = str(start_time)
            setTime.objects.create(name=time, day=instance, date=date, count=0)
