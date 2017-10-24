# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 19:56
from __future__ import unicode_literals

from django.db import migrations
import pgcrypto.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20171023_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='owner',
            field=pgcrypto.fields.EncryptedCharField(charset=b'utf-8', check_armor=True, cipher=b'AES', default='', versioned=False),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='phone_number',
            field=pgcrypto.fields.EncryptedCharField(charset=b'utf-8', check_armor=True, cipher=b'AES', default='', versioned=False),
        ),
    ]