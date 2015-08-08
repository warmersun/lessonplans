# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='LessonPlanPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('theme', wagtail.wagtailcore.fields.RichTextField(help_text='Set the theme or topic for the lesson. Is it about space and colonizing a planet? Is it dinosaurs? What is it?', blank=True)),
                ('introduction', wagtail.wagtailcore.fields.StreamField([('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='edit')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image / picture')), ('URL', wagtail.wagtailcore.blocks.URLBlock(help_text='Add itroductiory video that ste the theme', icon='link'))], help_text='blah')),
                ('introduction_length', models.DurationField()),
                ('new_tool', wagtail.wagtailcore.fields.StreamField([('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='edit')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image / picture')), ('URL', wagtail.wagtailcore.blocks.URLBlock(help_text='Add  video that explains the new tool', icon='link'))])),
                ('design_challenge', wagtail.wagtailcore.fields.StreamField([('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='edit')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image / picture')), ('URL', wagtail.wagtailcore.blocks.URLBlock(help_text='Add a video that will pose a deisgn challenge', icon='link'))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MethodCardPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('why', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('how', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('picture', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='lessonplanpage',
            name='method',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='home.MethodCardPage', null=True),
        ),
    ]
