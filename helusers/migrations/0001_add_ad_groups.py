# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('display_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ADGroupMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='helusers.ADGroup')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ad_groups', to='auth.Group')),
            ],
            options={
                'verbose_name': 'AD Group Mapping',
            },
        ),
        migrations.AlterUniqueTogether(
            name='adgroupmapping',
            unique_together=set([('group', 'ad_group')]),
        ),
    ]
