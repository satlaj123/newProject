# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('form', '0006_auto_20170720_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('filename', models.CharField(max_length=200)),
                ('file_type', models.CharField(max_length=100)),
                ('file_url', models.URLField(null=True, max_length=100, blank=True)),
                ('added_on', models.DateField(null=True, blank=True)),
                ('is_sharable', models.BooleanField(default=True)),
                ('active_yesno', models.BooleanField(default=True)),
                ('checkbox_id', models.CharField(null=True, max_length=50, blank=True)),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
                ('last_modified_by', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
