# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_bicicletas_bici_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bicicletas',
            old_name='bici',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='canciones',
            old_name='cancion',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='videoclips',
            old_name='videoclip',
            new_name='nombre',
        ),
    ]
