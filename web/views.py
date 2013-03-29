# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from web.models import city
from web.models import type_travel
from web.models import place

def index(request):
    cities_list = city.objects.order_by('name')
    types_list = type_travel.objects.order_by('name')
    context = {'cities_list':cities_list, 'types_list':types_list}
    #return HttpResponse("hola!!!!!!")
    return render(request,'web/index.html',context)
    
def itinerary(request):
    places_list = place.objects.order_by('name')
    context = {'places_list':places_list}
    return render(request, 'web/itinerary.html', context)