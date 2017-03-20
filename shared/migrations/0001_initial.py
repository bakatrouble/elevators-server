# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=256, unique=True, verbose_name='Имя пользователя')),
                ('group', models.CharField(choices=[('supervisor', 'Супервизор'), ('secretary', 'Секретарь-референт'), ('accounting', 'Сметно-договорной отдел'), ('testing', 'Испытательный центр')], max_length=20, verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(blank=True)),
                ('short_name', models.CharField(blank=True, max_length=256)),
                ('registration_address', models.TextField(blank=True)),
                ('location_address', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=256)),
                ('inn', models.CharField(blank=True, max_length=256)),
                ('kpp', models.CharField(blank=True, max_length=256)),
                ('account_number', models.CharField(blank=True, max_length=256)),
                ('bank', models.CharField(blank=True, max_length=256)),
                ('bik', models.CharField(blank=True, max_length=256)),
                ('ogrn', models.CharField(blank=True, max_length=256)),
                ('person_name', models.CharField(blank=True, max_length=256)),
                ('person_post', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=128, verbose_name='Имя')),
                ('patr_name', models.CharField(max_length=128, verbose_name='Отчество')),
            ],
            options={
                'verbose_name': 'специалист',
                'verbose_name_plural': 'специалисты',
            },
        ),
    ]
