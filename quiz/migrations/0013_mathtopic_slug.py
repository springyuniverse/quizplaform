# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-03-05 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_auto_20180305_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='mathtopic',
            name='slug',
            field=models.SlugField(default=True, max_length=40),
        ),
    ]
