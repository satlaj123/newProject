# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_sendmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodGroupMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lastModifiedDateTime', models.CharField(null=True, blank=True, max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='city',
            field=models.ForeignKey(blank=True, to='form.CityMaster', null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='country',
            field=models.ForeignKey(blank=True, to='form.CountryMaster', null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='state',
            field=models.ForeignKey(blank=True, to='form.StateMaster', null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='blood_group',
            field=models.ForeignKey(blank=True, to='form.BloodGroupMaster', null=True),
        ),
    ]
