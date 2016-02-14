# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20150320_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to=b'photos', verbose_name=b'picture', blank=True)),
                ('video', models.FileField(upload_to=b'videos', verbose_name=b'video', blank=True)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Videoclips',
        ),
        migrations.AlterField(
            model_name='bicicletas',
            name='imagen',
            field=models.ImageField(upload_to=b'photos', verbose_name=b'photos', blank=True),
            preserve_default=True,
        ),
    ]
