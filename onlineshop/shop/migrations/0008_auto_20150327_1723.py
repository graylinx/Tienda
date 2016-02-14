# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20150327_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicicletas',
            name='nombre2',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='canciones',
            name='nombre2',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='libros',
            name='nombre2',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
