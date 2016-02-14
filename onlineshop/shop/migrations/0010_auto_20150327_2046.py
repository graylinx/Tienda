# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20150327_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicicletas',
            name='ref',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='canciones',
            name='ref',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='libros',
            name='ref',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
