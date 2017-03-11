# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('short_name', models.CharField(max_length=256)),
                ('registration_address', models.TextField()),
                ('location_address', models.TextField()),
                ('phone', models.CharField(max_length=256)),
                ('inn', models.CharField(max_length=256)),
                ('kpp', models.CharField(max_length=256)),
                ('account_number', models.CharField(max_length=256)),
                ('bank', models.CharField(max_length=256)),
                ('bik', models.CharField(max_length=256)),
                ('ogrn', models.CharField(max_length=256)),
            ],
        ),
    ]