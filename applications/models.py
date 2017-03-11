from django.db import models
from django.apps import apps

from shared.models import Client


class ApplicationType(models.Model):
    name = models.CharField(max_length=256)
    hints = models.TextField(blank=True)
    application_template = models.TextField(blank=True)
    contract_template = models.TextField(blank=True)
    order_template = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    date = models.DateField()
    creation_date = models.DateField(auto_now_add=True)
    type = models.ForeignKey(ApplicationType)
    client = models.ForeignKey(Client)

    def get_contract(self):
        return apps.get_model('contracts', 'Contract').objects.filter(application=self).first()


class ApplicationEntry(models.Model):
    application = models.ForeignKey(Application, related_name='entries')
    address_oblast = models.CharField(max_length=256, blank=True)
    address_raion = models.CharField(max_length=256, blank=True)
    address_city = models.CharField(max_length=256, blank=True)
    address_street = models.CharField(max_length=256, blank=True)
    address_house = models.CharField(max_length=10, blank=True)
    address_building = models.CharField(max_length=10, blank=True)
    address_letter = models.CharField(max_length=10, blank=True)
    purpose = models.CharField(max_length=256, blank=True)
    number = models.CharField(max_length=256, blank=True)
    maker = models.CharField(max_length=256, blank=True)
    load = models.CharField(max_length=256, blank=True)
    stops = models.IntegerField(blank=True)
    speed = models.CharField(max_length=256, blank=True)
    date = models.DateField(blank=True)
    replacements = models.TextField(blank=True)
    deadline = models.CharField(max_length=256, blank=True)
