# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_auto_20170701_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendMessage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
    ]
