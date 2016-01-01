# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 04:29
from __future__ import unicode_literals

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoro', '0003_auto_20151106_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='category',
            field=models.CharField(blank=True, max_length=32, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='duration',
            field=models.IntegerField(verbose_name='duration'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='title',
            field=models.CharField(max_length=32, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='pomodoro',
            name='category',
            field=models.CharField(blank=True, max_length=32, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='pomodoro',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='start time'),
        ),
        migrations.AlterField(
            model_name='pomodoro',
            name='duration',
            field=models.IntegerField(verbose_name='duration'),
        ),
        migrations.AlterField(
            model_name='pomodoro',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pomodoros', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='pomodoro',
            name='title',
            field=models.CharField(max_length=32, verbose_name='title'),
        ),
    ]
