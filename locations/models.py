from django.db import models


class TestLocationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(disable=True)


class TestLocation(models.Model):
    pass
    location_name = models.CharField('Location Name', max_length=50)
    location_address = models.TextField('Location Address', max_length=300)
    disable = models.BooleanField(default=False)

    objects = TestLocationManager()

    def __str__(self):
        return self.location_name
