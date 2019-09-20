from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Paragens, c6, c9
# Create your views here.
class HomePageView(TemplateView):
	template_name = 'index.html'

def Paragens_dataset(request):
	ParagensV = serialize('geojson', Paragens.objects.all())
	return HttpResponse(ParagensV, content_type='json')

def c6_dataset(request):
	c6V = serialize('geojson', c6.objects.all())
	return HttpResponse(c6V, content_type='json')

def c9_dataset(request):
	c9V = serialize('geojson', c9.objects.all())
	return HttpResponse(c9V, content_type='json')