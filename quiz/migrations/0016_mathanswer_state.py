# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-03-25 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_mathanswer_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='mathanswer',
            name='state',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
