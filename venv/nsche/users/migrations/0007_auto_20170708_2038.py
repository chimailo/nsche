# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20170708_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='part',
            field=models.IntegerField(choices=[(100, 1), (200, 2), (300, 3), (400, 4), (500, 5)], default=1),
        ),
    ]
