from django.db import models

from applications.models import Application


class Contract(models.Model):
    application = models.ForeignKey(Application)
    number = models.CharField(max_length=256)
    date = models.DateField(blank=True)
    finish_date = models.DateField(blank=True)
    price = models.FloatField()
    terms = models.TextField(blank=True)
    poa = models.BooleanField(default=False)  # доверенность
    poa_number = models.CharField(max_length=256)
    poa_date = models.DateField()
