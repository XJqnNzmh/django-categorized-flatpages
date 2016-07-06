# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cflatpages', '0003_auto_20160629_1128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['num'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
