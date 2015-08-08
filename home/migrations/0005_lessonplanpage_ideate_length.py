# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20150808_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonplanpage',
            name='ideate_length',
            field=models.PositiveSmallIntegerField(default=1, help_text='in minutes'),
            preserve_default=False,
        ),
    ]
