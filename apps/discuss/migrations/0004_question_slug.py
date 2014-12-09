# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0003_remove_question_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2014, 12, 8, 4, 34, 10, 110008, tzinfo=utc), unique=True, editable=False),
            preserve_default=False,
        ),
    ]
