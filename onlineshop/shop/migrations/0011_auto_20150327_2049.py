# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20150327_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bicicletas',
            name='ref',
        ),
        migrations.RemoveField(
            model_name='canciones',
            name='ref',
        ),
        migrations.RemoveField(
            model_name='libros',
            name='ref',
        ),
    ]
