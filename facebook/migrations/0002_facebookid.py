# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pi_id', models.IntegerField()),
                ('fb_id', models.IntegerField()),
            ],
        ),
    ]
