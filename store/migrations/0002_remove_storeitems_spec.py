# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 00:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storeitems',
            name='spec',
        ),
    ]
