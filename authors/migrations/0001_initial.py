# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'ordering': [b'name'],
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
            },
            bases=(models.Model,),
        ),
    ]
