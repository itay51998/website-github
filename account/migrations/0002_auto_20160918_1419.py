# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='style',
            field=models.IntegerField(),
        ),
    ]
