from django.contrib import admin
from .models import teste, Paragens, c6, c9
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class testeAdmin (LeafletGeoAdmin):
	list_display =('name', 'location')

class ParagensAdmin (LeafletGeoAdmin):
	list_display =('name', 'ql_key', 'sym')

class c6Admin (LeafletGeoAdmin):
	list_display =('codrota', 'rota', 'carreira', 'viauso', 'nomecorred')

class c9Admin (LeafletGeoAdmin):
	list_display =('codrota', 'rota', 'carreira', 'viauso', 'nomecorred')

admin.site.register(teste, testeAdmin)
admin.site.register (Paragens, ParagensAdmin)
admin.site.register (c6, c6Admin)
admin.site.register (c9, c9Admin)