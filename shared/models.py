from django.db import models
from django.contrib.auth.models import AbstractUser


class Client(models.Model):
    full_name = models.TextField(blank=True)
    short_name = models.CharField(max_length=256, blank=True)
    registration_address = models.TextField(blank=True)
    location_address = models.TextField(blank=True)
    phone = models.CharField(max_length=256, blank=True)
    inn = models.CharField(max_length=256, blank=True)
    kpp = models.CharField(max_length=256, blank=True)
    account_number = models.CharField(max_length=256, blank=True)
    bank = models.CharField(max_length=256, blank=True)
    bik = models.CharField(max_length=256, blank=True)
    ogrn = models.CharField(max_length=256, blank=True)
    person_name = models.CharField(max_length=256, blank=True)
    person_post = models.CharField(max_length=256, blank=True)  # должность

    def __str__(self):
        return self.short_name


class Specialist(models.Model):
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    patr_name = models.CharField(max_length=128)

    def __str__(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.patr_name)


class User(AbstractUser):
    SECRETARY_GROUP = 'secretary'
    ACCOUNTING_GROUP = 'accounting'
    TESTING_GROUP = 'testing'
    # TESTING_ACCOUNTING_GROUP = 'testing_accounting'

    GROUP_CHOICES = (
        (SECRETARY_GROUP, 'Секретарь-референт'),
        (ACCOUNTING_GROUP, 'Сметно-договорной отдел'),
        (TESTING_GROUP, 'Испытательный центр'),
    )

    group = models.CharField(max_length=20, choices=GROUP_CHOICES)
