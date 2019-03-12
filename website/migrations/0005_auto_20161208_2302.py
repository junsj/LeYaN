# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_one'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('title_img', models.CharField(max_length=64, null=True)),
                ('image', models.CharField(max_length=100, null=True)),
                ('text', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(default='', null=True)),
                ('span', models.CharField(max_length=64, null=True)),
                ('source', models.CharField(max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField(unique=True)),
                ('cname', models.CharField(max_length=32)),
                ('cgroup', models.CharField(max_length=32, default='')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='website.Category'),
        ),
    ]
