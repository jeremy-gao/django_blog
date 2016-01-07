# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.CharField(max_length=11)),
                ('city', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='context',
            field=DjangoUeditor.models.UEditorField(),
        ),
    ]
