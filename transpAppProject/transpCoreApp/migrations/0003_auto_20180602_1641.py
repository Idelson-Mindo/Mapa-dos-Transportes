# Generated by Django 2.0.6 on 2018-06-02 14:41

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transpCoreApp', '0002_auto_20180602_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teste',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]