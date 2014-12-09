# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0002_auto_20141207_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='slug',
        ),
    ]
