# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20150313_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicicletas',
            name='bici_imagen',
            field=models.ImageField(default=datetime.datetime(2015, 3, 14, 12, 17, 27, 207198, tzinfo=utc), upload_to=b'photos/'),
            preserve_default=False,
        ),
    ]
