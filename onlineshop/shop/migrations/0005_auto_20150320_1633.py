# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20150318_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bicicletas',
            old_name='bici_descripcion',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='bicicletas',
            old_name='bici_color',
            new_name='tipo',
        ),
        migrations.RenameField(
            model_name='canciones',
            old_name='cancion_artista',
            new_name='tipo',
        ),
        migrations.RenameField(
            model_name='videoclips',
            old_name='videoclip_artista',
            new_name='tipo',
        ),
        migrations.RemoveField(
            model_name='bicicletas',
            name='bici_imagen',
        ),
        migrations.RemoveField(
            model_name='bicicletas',
            name='bici_tipo',
        ),
        migrations.RemoveField(
            model_name='canciones',
            name='cancion_titulo',
        ),
        migrations.RemoveField(
            model_name='videoclips',
            name='videoclip_titulo',
        ),
        migrations.AddField(
            model_name='bicicletas',
            name='imagen',
            field=models.ImageField(upload_to=b'photos', verbose_name=b'picture', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bicicletas',
            name='precio',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bicicletas',
            name='video',
            field=models.FileField(upload_to=b'videos', verbose_name=b'video', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='canciones',
            name='descripcion',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='canciones',
            name='imagen',
            field=models.ImageField(upload_to=b'photos', verbose_name=b'picture', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='canciones',
            name='precio',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='canciones',
            name='video',
            field=models.FileField(upload_to=b'videos', verbose_name=b'video', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videoclips',
            name='descripcion',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videoclips',
            name='imagen',
            field=models.ImageField(upload_to=b'photos', verbose_name=b'picture', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videoclips',
            name='precio',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videoclips',
            name='video',
            field=models.FileField(upload_to=b'videos', verbose_name=b'video', blank=True),
            preserve_default=True,
        ),
    ]
