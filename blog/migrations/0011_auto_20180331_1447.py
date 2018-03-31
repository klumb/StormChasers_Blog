# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-31 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_response_post_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='response_post',
            name='author',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='top_post',
            name='author',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='response_post',
            name='top_post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog.top_post'),
        ),
    ]
