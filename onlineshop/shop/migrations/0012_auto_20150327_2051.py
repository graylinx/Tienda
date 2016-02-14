# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20150327_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicicletas',
            name='ref',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='canciones',
            name='ref',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libros',
            name='ref',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
