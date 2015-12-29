# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link_title', models.CharField(max_length=40)),
                ('link_url', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('context', models.TextField()),
                ('author', models.CharField(max_length=20)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('tag', models.CharField(max_length=12)),
                ('cid', models.ForeignKey(to='blog.Category')),
            ],
        ),
    ]
