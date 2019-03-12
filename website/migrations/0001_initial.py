# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', max_length=60)),
                ('source', models.CharField(null=True, max_length=50)),
                ('description', models.CharField(null=True, max_length=100)),
                ('group', models.CharField(default='', max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pics',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(null=True, max_length=100, default='')),
                ('url', models.CharField(null=True, max_length=100)),
                ('pixs', models.CharField(null=True, max_length=20)),
                ('sortkey', models.CharField(null=True, max_length=20)),
                ('text', models.TextField(null=True, default='')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(default='', to='website.Albums')),
            ],
        ),
    ]
