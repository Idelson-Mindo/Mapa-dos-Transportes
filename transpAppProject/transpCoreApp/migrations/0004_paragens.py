# Generated by Django 2.0.6 on 2018-06-02 15:27

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transpCoreApp', '0003_auto_20180602_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paragens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ele', models.FloatField()),
                ('time', models.CharField(max_length=24)),
                ('magvar', models.FloatField()),
                ('geoidheigh', models.FloatField()),
                ('name', models.CharField(max_length=254)),
                ('cmt', models.CharField(max_length=254)),
                ('desc', models.CharField(max_length=254)),
                ('src', models.CharField(max_length=254)),
                ('link1_href', models.CharField(max_length=254)),
                ('link1_text', models.CharField(max_length=254)),
                ('link1_type', models.CharField(max_length=254)),
                ('link2_href', models.CharField(max_length=254)),
                ('link2_text', models.CharField(max_length=254)),
                ('link2_type', models.CharField(max_length=254)),
                ('sym', models.CharField(max_length=254)),
                ('typ', models.CharField(max_length=254)),
                ('fix', models.CharField(max_length=254)),
                ('sat', models.BigIntegerField()),
                ('hdop', models.FloatField()),
                ('vdop', models.FloatField()),
                ('pdop', models.FloatField()),
                ('ageofdgpsd', models.FloatField()),
                ('dgpsid', models.BigIntegerField()),
                ('ql_key', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
    ]