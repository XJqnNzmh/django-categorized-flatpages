# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cflatpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cflatpage',
            name='pos',
            field=models.IntegerField(default=0, verbose_name='position', blank=True),
        ),
        migrations.AlterField(
            model_name='cflatpage',
            name='category',
            field=mptt.fields.TreeForeignKey(related_name='page_category', verbose_name='category', to='cflatpages.Category'),
        ),
        migrations.AlterField(
            model_name='cflatpage',
            name='description',
            field=models.CharField(max_length=255, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='cflatpage',
            name='keywords',
            field=models.CharField(max_length=100, verbose_name='keywords', blank=True),
        ),
    ]
