from django.db import models

from shared.models import Specialist


class Order(models.Model):
    application = models.ForeignKey('applications.Application')
    number = models.CharField(max_length=256, blank=True)
    date = models.DateField(blank=True)
    to_date = models.DateField(blank=True)
    act_date = models.DateField(blank=True)
    controller = models.CharField(max_length=256, blank=True)
    head_specialist = models.ForeignKey(Specialist, null=True, related_name='heading_orders')
    specialists = models.ManyToManyField(Specialist, blank=True)
