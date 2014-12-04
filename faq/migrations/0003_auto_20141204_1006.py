# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_auto_20141123_1455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ('ordering', 'title', 'slug'), 'get_latest_by': 'modified', 'verbose_name': 'topic', 'verbose_name_plural': 'topics'},
        ),
        migrations.AddField(
            model_name='topic',
            name='ordering',
            field=models.PositiveSmallIntegerField(default=0, help_text='An integer used to order the topic             amongst others. If not given this             topic will be last in the list.', db_index=True, verbose_name='ordering', blank=True),
            preserve_default=False,
        ),
    ]
