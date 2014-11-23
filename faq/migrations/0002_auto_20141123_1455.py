# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_de',
            field=models.TextField(default=b'', verbose_name='answer DE', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='question_de',
            field=models.CharField(default=b'', max_length=255, verbose_name='question DE', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='topic',
            name='description_de',
            field=models.TextField(default=b'', help_text='A short description of this topic.', verbose_name='description DE', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='topic',
            name='title_de',
            field=models.CharField(default=b'', max_length=255, verbose_name='title DE', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(verbose_name='answer EN'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=255, verbose_name='question EN'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(help_text='A short description of this topic.', verbose_name='description EN', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title EN'),
            preserve_default=True,
        ),
    ]
