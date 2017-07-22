# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20170701_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='aditya',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='amit',
            new_name='pincode',
        ),
    ]
