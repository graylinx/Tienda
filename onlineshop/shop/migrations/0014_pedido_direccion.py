# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='direccion',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
