# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 01:02
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20161115_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(icon='title')), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock()), ('source', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.URLBlock(required=False))))), ('table', wagtail.contrib.table_block.blocks.TableBlock()))),
        ),
    ]
