# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-09 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=30)),
                ('urecieve', models.CharField(default='', max_length=20)),
                ('uaddress', models.CharField(max_length=40)),
                ('uyoubian', models.CharField(default='', max_length=6)),
                ('uphone', models.CharField(default='', max_length=11)),
            ],
        ),
    ]