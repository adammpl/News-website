# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20160831_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
