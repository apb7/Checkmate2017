# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-17 08:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20170817_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='number',
            new_name='points',
        ),
    ]