# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0012_profileinfo_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='texts',
            field=models.TextField(blank=True, null=True),
        ),
    ]
