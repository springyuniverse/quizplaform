# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-03-25 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_auto_20180306_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='mathanswer',
            name='answer',
            field=models.CharField(blank=True, default=b'', max_length=200, null=True),
        ),
    ]