# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20161205_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='ONE',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('url', models.CharField(max_length=100, default='')),
                ('img', models.CharField(max_length=100, default='')),
                ('local_img', models.CharField(max_length=100, default='')),
                ('text', models.TextField(default='')),
                ('dom', models.IntegerField(default='')),
                ('may', models.CharField(max_length=20, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
