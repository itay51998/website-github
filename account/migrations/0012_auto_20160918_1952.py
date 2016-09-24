# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20160918_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='usersN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
                ('nickname', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=45)),
                ('password', models.CharField(max_length=32)),
                ('type', models.CharField(max_length=8)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=1)),
            ],
        ),
        migrations.DeleteModel(
            name='accounts',
        ),
    ]
