# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-03 20:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0026_toptieragency_justification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legalentityofficers',
            name='legal_entity',
        ),
        migrations.DeleteModel(
            name='LegalEntityOfficers',
        ),
    ]
