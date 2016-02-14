# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cancion', models.CharField(max_length=50)),
                ('cancion_titulo', models.CharField(max_length=50)),
                ('cancion_artista', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Videoclips',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('videoclip', models.CharField(max_length=50)),
                ('videoclip_titulo', models.CharField(max_length=50)),
                ('videoclip_artista', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bicicletas',
            name='bici_descripcion',
            field=models.TextField(default=datetime.datetime(2015, 3, 13, 19, 41, 26, 340317, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bicicletas',
            name='bici_color',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bicicletas',
            name='bici_tipo',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
