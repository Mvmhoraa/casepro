# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-17 14:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('msgs', '0054_auto_20161201_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='actioned_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actioned_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='last_action',
            field=models.DateTimeField(auto_now=True, help_text='Last action taken on this message', null=True),
        ),
    ]
