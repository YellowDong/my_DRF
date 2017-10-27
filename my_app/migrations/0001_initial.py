# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IpoInfo',
            fields=[
                ('security_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('security_name', models.CharField(blank=True, max_length=20, null=True)),
                ('total_initial_issue', models.IntegerField(blank=True, null=True)),
                ('actual_fundraised', models.FloatField(blank=True, null=True)),
                ('offline_issue_date', models.DateField(blank=True, null=True)),
                ('online_issue_date', models.DateField(blank=True, null=True)),
                ('issue_price', models.FloatField(blank=True, null=True)),
                ('total_issued', models.FloatField(blank=True, null=True)),
                ('ipo_pe_ratio', models.FloatField(blank=True, null=True)),
                ('offline_circulation', models.FloatField(blank=True, null=True)),
                ('online_circulation', models.FloatField(blank=True, null=True)),
                ('online_purchase_limit', models.FloatField(blank=True, null=True)),
                ('success_rate', models.CharField(blank=True, max_length=50, null=True)),
                ('success_rate_date', models.DateField(blank=True, null=True)),
                ('listed_date', models.DateField(blank=True, null=True)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('payment_end_date', models.DateField(blank=True, null=True)),
                ('crawl_timestamp', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ipo_info',
                'managed': False,
            },
        ),
    ]