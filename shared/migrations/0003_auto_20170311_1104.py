# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0002_auto_20170307_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='person_name',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='client',
            name='person_post',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
