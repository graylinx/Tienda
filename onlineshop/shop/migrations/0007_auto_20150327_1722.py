# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20150320_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicicletas',
            name='nombre2',
            field=models.TextField(default=0, verbose_name=b'hola'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='canciones',
            name='nombre2',
            field=models.TextField(default=0, verbose_name=b'hola'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libros',
            name='nombre2',
            field=models.TextField(default=0, verbose_name=b'hola'),
            preserve_default=False,
        ),
    ]
