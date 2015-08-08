# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20150808_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonplanpage',
            name='define_length',
            field=models.PositiveSmallIntegerField(default=1, help_text='in minutes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lessonplanpage',
            name='empathize_length',
            field=models.PositiveSmallIntegerField(default=1, help_text='in minutes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lessonplanpage',
            name='prototype_length',
            field=models.PositiveSmallIntegerField(default=1, help_text='in minutes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lessonplanpage',
            name='test_length',
            field=models.PositiveSmallIntegerField(default=1, help_text='in minutes'),
            preserve_default=False,
        ),
    ]
