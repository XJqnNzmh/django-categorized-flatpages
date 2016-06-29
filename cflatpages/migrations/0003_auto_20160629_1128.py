# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cflatpages', '0002_auto_20160629_0803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cflatpage',
            options={'ordering': ['num'], 'verbose_name': 'categorized flatpage', 'verbose_name_plural': 'categorized flatpages'},
        ),
        migrations.RemoveField(
            model_name='cflatpage',
            name='pos',
        ),
        migrations.AddField(
            model_name='cflatpage',
            name='num',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='order number'),
        ),
    ]
