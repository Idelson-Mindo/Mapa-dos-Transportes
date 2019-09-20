import os
from django.contrib.gis.utils import LayerMapping
from .models import Paragens, c6, c9


# Auto-generated `LayerMapping` dictionary for Paragens.shp model
paragens_mapping = {
    'ele': 'ele',
    'time': 'time',
    'magvar': 'magvar',
    'geoidheigh': 'geoidheigh',
    'name': 'name',
    'cmt': 'cmt',
    'desc': 'desc',
    'src': 'src',
    'link1_href': 'link1_href',
    'link1_text': 'link1_text',
    'link1_type': 'link1_type',
    'link2_href': 'link2_href',
    'link2_text': 'link2_text',
    'link2_type': 'link2_type',
    'sym': 'sym',
    'type': 'type',
    'fix': 'fix',
    'sat': 'sat',
    'hdop': 'hdop',
    'vdop': 'vdop',
    'pdop': 'pdop',
    'ageofdgpsd': 'ageofdgpsd',
    'dgpsid': 'dgpsid',
    'ql_key': 'ql_key',
    'geom': 'MULTIPOINT25D',
}

Paragens_shp = os.path . abspath(os.path.join(os.path.dirname(__file__),'data/paragens.shp'))

def runParagens(verbose=True):
	lmParagens = LayerMapping(Paragens, Paragens_shp, paragens_mapping, transform=False, encoding='iso-8859-1')
	lmParagens.save (strict=True, verbose = verbose)

c6_mapping = {
    'objectid': 'OBJECTID',
    'codrota': 'CodRota',
    'rota': 'Rota',
    'carreira': 'Carreira',
    'viauso': 'ViaUSO',
    'nomecorred': 'NomeCorred',
    'codoperado': 'CodOperado',
    'codbairro': 'CodBairro',
    'coddistrit': 'CodDistrit',
    'codvia': 'CodVia',
    'shape_leng': 'SHAPE_Leng',
    'codseccao': 'CodSeccao',
    'geom': 'MULTILINESTRING',
}

c6_shp = os.path . abspath(os.path.join(os.path.dirname(__file__),'data/carreira6EMTPM.shp'))

def runc6(verbose=True):
	lmC6 = LayerMapping(c6, c6_shp, c6_mapping, transform=False, encoding='iso-8859-1')
	lmC6.save (strict=True, verbose = verbose)

c9_mapping = {
    'objectid': 'OBJECTID',
    'codrota': 'CodRota',
    'rota': 'Rota',
    'carreira': 'Carreira',
    'viauso': 'ViaUSO',
    'nomecorred': 'NomeCorred',
    'codoperado': 'CodOperado',
    'codbairro': 'CodBairro',
    'coddistrit': 'CodDistrit',
    'codvia': 'CodVia',
    'shape_leng': 'SHAPE_Leng',
    'codseccao': 'CodSeccao',
    'geom': 'MULTILINESTRING',
}

c9_shp = os.path . abspath(os.path.join(os.path.dirname(__file__),'data/carreira9EMTPM.shp'))

def runc9(verbose=True):
	lmC9 = LayerMapping(c9, c9_shp, c9_mapping, transform=False, encoding='iso-8859-1')
	lmC9.save (strict=True, verbose = verbose)