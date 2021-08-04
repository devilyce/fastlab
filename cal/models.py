from django.db import models


class setYear(models.Model):
    name = models.IntegerField()

    def __str__(self):
        return str(self.name)


class setMonth(models.Model):
    name = models.CharField(max_length=30)
    year = models.ForeignKey(setYear, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return str(self.year) + ' ' + str(self.name)

    class Meta:
        ordering = ['date']


class setDay(models.Model):
    name = models.IntegerField()
    month = models.ForeignKey(setMonth, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.month) + ' ' + str(self.name)

    class Meta:
        ordering = ['date']


class setTime(models.Model):
    name = models.TimeField()
    day = models.ForeignKey(setDay, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name) + ' ' + str(self.day)


class timeChoice(models.Model):
    name = models.TimeField()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
