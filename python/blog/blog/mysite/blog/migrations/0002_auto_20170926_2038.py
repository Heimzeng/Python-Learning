# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 12:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogsPost',
            new_name='Article',
        ),
    ]