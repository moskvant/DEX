# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-08 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dex', '0003_remove_orders_ordernum'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='FIRM',
            field=models.CharField(default='deletefirm', max_length=25),
            preserve_default=False,
        ),
    ]
