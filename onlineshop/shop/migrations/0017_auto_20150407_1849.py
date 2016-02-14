# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_pedido_correo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='direccion',
        ),
        migrations.AddField(
            model_name='pedido',
            name='numero',
            field=models.IntegerField(default=0, max_length=9),
            preserve_default=False,
        ),
    ]
