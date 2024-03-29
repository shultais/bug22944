# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
            ],
            options={
                'ordering': [b'title'],
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
            bases=(models.Model,),
        ),
    ]
