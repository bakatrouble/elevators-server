# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.Client')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_oblast', models.CharField(max_length=256)),
                ('address_raion', models.CharField(max_length=256)),
                ('address_city', models.CharField(max_length=256)),
                ('address_street', models.CharField(max_length=256)),
                ('address_house', models.CharField(max_length=10)),
                ('address_building', models.CharField(max_length=10)),
                ('address_letter', models.CharField(max_length=10)),
                ('purpose', models.CharField(max_length=256)),
                ('number', models.CharField(max_length=256)),
                ('maker', models.CharField(max_length=256)),
                ('load', models.CharField(max_length=256)),
                ('stops', models.IntegerField()),
                ('speed', models.CharField(max_length=256)),
                ('date', models.DateField()),
                ('replacements', models.TextField()),
                ('deadline', models.CharField(max_length=256)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='applications.Application')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('hints', models.TextField()),
                ('application_template', models.TextField(blank=True)),
                ('contract_template', models.TextField(blank=True)),
                ('order_template', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.ApplicationType'),
        ),
    ]