# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-14 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_calls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('Email', models.TextField()),
                ('phone_number', models.TextField()),
                ('Language', models.TextField()),
                ('Currency', models.TextField()),
            ],
        ),
    ]
