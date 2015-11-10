# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('original', models.ImageField(upload_to=b'')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=4000)),
                ('preview', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
        ),
    ]
