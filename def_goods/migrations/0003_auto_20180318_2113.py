# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-18 13:13
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('def_goods', '0002_auto_20180313_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gdescribe',
            field=tinymce.models.HTMLField(max_length=1000),
        ),
    ]
