# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bicicletas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bici', models.CharField(max_length=50)),
                ('bici_color', models.TextField()),
                ('bici_tipo', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
