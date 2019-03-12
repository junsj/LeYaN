# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20161208_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='title_img',
        ),
    ]
