# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('phone', models.TextField(max_length=15, blank=True)),
                ('can_model', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'DeepScrub Registration',
                'verbose_name_plural': 'DeepScrub Registration',
            },
        ),
    ]
