# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-11 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=128)),
                ('sal', models.FloatField()),
            ],
        ),
    ]