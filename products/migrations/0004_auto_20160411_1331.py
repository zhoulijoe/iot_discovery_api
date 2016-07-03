# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20160322_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('name', 'company')]),
        ),
    ]