from django.db import models

from accounts.models import Account
from contracts.models import Contract
from orders.models import Order
from shared.models import Client


class ApplicationType(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    # hints = models.TextField(blank=True, verbose_name='Подсказки')
    application_template = models.TextField(blank=True, verbose_name='Шаблон печати заявки')
    contract_template = models.TextField(blank=True, verbose_name='Шаблон печати договора')
    account_template = models.TextField(blank=True, verbose_name='Шаблон печати счета')
    order_template = models.TextField(blank=True, verbose_name='Шаблон печати приказа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тип заявки'
        verbose_name_plural = 'типы заявок'


class Application(models.Model):
    date = models.DateField()
    creation_date = models.DateField(auto_now_add=True)
    type = models.ForeignKey(ApplicationType)
    client = models.ForeignKey(Client)

    def get_contract(self):
        return Contract.objects.filter(application=self).first()

    def get_account(self):
        return Account.objects.filter(application=self).first()

    def get_order(self):
        return Order.objects.filter(application=self).first()


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
