# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 06:01
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20160322_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]
