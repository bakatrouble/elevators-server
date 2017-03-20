from django.db import models


class Contract(models.Model):
    application = models.ForeignKey('applications.Application')
    number = models.CharField(max_length=256, blank=True)
    date = models.DateField(blank=True)
    price = models.FloatField()
    terms = models.TextField(blank=True)
    poa_client = models.BooleanField(default=False)  # доверенность
    poa_client_number = models.CharField(max_length=256, blank=True)
    poa_client_date = models.DateField(blank=True)
    poa_contractor = models.BooleanField(default=False)  # доверенность
    poa_contractor_number = models.CharField(max_length=256, blank=True)
    poa_contractor_date = models.DateField(blank=True)
