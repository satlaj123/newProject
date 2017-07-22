# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20170701_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='aditya',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='amit',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='isProfileComplete',
            field=models.BooleanField(default=False),
        ),
    ]
