# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='account_number',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='client',
            name='bank',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='client',
            name='bik',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='client',
            name='full_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='inn',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='client',
            name='kpp',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='client',
            name='location_address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='ogrn',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='client',
            name='registration_address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='short_name',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
