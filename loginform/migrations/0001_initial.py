# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('roll_no', models.CharField(max_length=200)),
                ('pic', models.ImageField(upload_to='', verbose_name='initial_picture')),
            ],
        ),
    ]
