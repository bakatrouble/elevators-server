# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=256)),
                ('date', models.DateField(blank=True)),
                ('to_date', models.DateField(blank=True)),
                ('act_date', models.DateField(blank=True)),
                ('controller', models.CharField(blank=True, max_length=256)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.Application')),
            ],
        ),
    ]
