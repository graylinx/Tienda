# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20150327_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bicicletas',
            name='nombre2',
        ),
        migrations.RemoveField(
            model_name='canciones',
            name='nombre2',
        ),
        migrations.RemoveField(
            model_name='libros',
            name='nombre2',
        ),
        migrations.AddField(
            model_name='bicicletas',
            name='ref',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='canciones',
            name='ref',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libros',
            name='ref',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=0),
            preserve_default=False,
        ),
    ]
