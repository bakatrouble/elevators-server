from django.db import models


class Contract(models.Model):
    application = models.ForeignKey('applications.Application')
    number = models.CharField(max_length=256)
    date = models.DateField(blank=True)
    finish_date = models.DateField(blank=True)
    price = models.FloatField()
    terms = models.TextField(blank=True)
    poa = models.BooleanField(default=False)  # доверенность
    poa_number = models.CharField(max_length=256)
    poa_date = models.DateField()
