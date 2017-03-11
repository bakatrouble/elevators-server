from django.db import models


class Account(models.Model):
    application = models.ForeignKey('applications.Application')
    number = models.CharField(max_length=256, blank=True)
    date = models.DateField(blank=True)
