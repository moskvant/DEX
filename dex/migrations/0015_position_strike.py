# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-15 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dex', '0014_position_sec_underlying'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='STRIKE',
            field=models.FloatField(default=0.0),
        ),
    ]
