# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default=django.utils.datetime_safe.date.today, unique=True, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
