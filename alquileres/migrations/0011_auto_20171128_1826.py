# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquileres', '0010_auto_20171128_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]