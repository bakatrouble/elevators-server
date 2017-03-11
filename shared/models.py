from django.db import models


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
