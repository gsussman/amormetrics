# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-08 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0010_auto_20180104_0354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('religion', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]