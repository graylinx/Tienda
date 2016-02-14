# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20150407_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='numero',
            field=models.CharField(max_length=9),
            preserve_default=True,
        ),
    ]
