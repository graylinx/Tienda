# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20150407_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='fecha',
        ),
    ]
