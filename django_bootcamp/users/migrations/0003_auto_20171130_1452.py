# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171128_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='shipping_city',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='user',
            name='shipping_country',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='user',
            name='shipping_first_name',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='user',
            name='shipping_last_name',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='user',
            name='shipping_phone',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='user',
            name='shipping_state',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='user',
            name='shipping_street',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='user',
            name='shipping_zip',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
