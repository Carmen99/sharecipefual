# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='ímages/None/no-img.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='preview_text',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
