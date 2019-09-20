from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager


# Create your models here.
class teste (models.Model):
	name = models.CharField(max_length=20)
	location = models.PointField(srid=4326)
	objects = GeoManager()

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural='teste'

class Paragens(models.Model):
    ele = models.FloatField()
    time = models.CharField(max_length=24)
    magvar = models.FloatField()
    geoidheigh = models.FloatField()
    name = models.CharField(max_length=254)
    cmt = models.CharField(max_length=254)
    desc = models.CharField(max_length=254)
    src = models.CharField(max_length=254)
    link1_href = models.CharField(max_length=254)
    link1_text = models.CharField(max_length=254)
    link1_type = models.CharField(max_length=254)
    link2_href = models.CharField(max_length=254)
    link2_text = models.CharField(max_length=254)
    link2_type = models.CharField(max_length=254)
    sym = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    fix = models.CharField(max_length=254)
    sat = models.BigIntegerField()
    hdop = models.FloatField()
    vdop = models.FloatField()
    pdop = models.FloatField()
    ageofdgpsd = models.FloatField()
    dgpsid = models.BigIntegerField()
    ql_key = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
    	return self.Paragens

class c6(models.Model):
    objectid = models.BigIntegerField()
    codrota = models.CharField(max_length=50)
    rota = models.CharField(max_length=50)
    carreira = models.CharField(max_length=50)
    viauso = models.CharField(max_length=50)
    nomecorred = models.CharField(max_length=50)
    codoperado = models.CharField(max_length=50)
    codbairro = models.CharField(max_length=50)
    coddistrit = models.CharField(max_length=50)
    codvia = models.CharField(max_length=50)
    shape_leng = models.FloatField()
    codseccao = models.CharField(max_length=50)
    geom = models.MultiLineStringField(srid=4326)

    def __unicode__(self):
    	return self.c6

class c9(models.Model):
    objectid = models.BigIntegerField()
    codrota = models.CharField(max_length=50)
    rota = models.CharField(max_length=50)
    carreira = models.CharField(max_length=50)
    viauso = models.CharField(max_length=50)
    nomecorred = models.CharField(max_length=50)
    codoperado = models.CharField(max_length=50)
    codbairro = models.CharField(max_length=50)
    coddistrit = models.CharField(max_length=50)
    codvia = models.CharField(max_length=50)
    shape_leng = models.FloatField()
    codseccao = models.CharField(max_length=50)
    geom = models.MultiLineStringField(srid=4326)


    def __unicode__(self):
    	return self.c9