# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-06 16:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_useranswer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]
