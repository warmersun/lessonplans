# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150808_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonplanpage',
            name='introduction_length',
            field=models.PositiveSmallIntegerField(help_text='in minutes'),
        ),
    ]
