# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20161204_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albums',
            old_name='group',
            new_name='group_id',
        ),
    ]
