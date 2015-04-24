# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orgs', '0010_auto_20150424_1427'),
        ('cases', '0004_auto_20150421_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('messages', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('action', models.CharField(max_length=1, choices=[('F', 'Flag'), ('N', 'Un-flag'), ('L', 'Label'), ('A', 'Archive')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(related_name='message_actions', to=settings.AUTH_USER_MODEL)),
                ('label', models.ForeignKey(to='cases.Label', null=True)),
                ('org', models.ForeignKey(related_name='message_actions', verbose_name='Organization', to='orgs.Org')),
            ],
        ),
        migrations.RunSQL(
            'CREATE INDEX cases_messageaction_messages_idx ON cases_messageaction USING GIN ("messages");'
        ),
        migrations.AlterModelOptions(
            name='caseaction',
            options={},
        ),
    ]
