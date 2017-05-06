# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-05 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20170503_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='grade',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='score',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
