# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-17 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('def_order', '0002_auto_20180316_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='pay_way',
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='water_number',
            field=models.CharField(max_length=20),
        ),
    ]
