# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0011_religion'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileinfo',
            name='package',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
