# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from web.models import city
from web.models import type_travel
from web.models import place
from web.models import budget

def index(request):
    cities_list = city.objects.order_by('name')
    types_list = type_travel.objects.order_by('name')
    budget_list = budget.objects.order_by('name')
    context = {'cities_list':cities_list, 'types_list':types_list, 'budget_list':budget_list}
    #return HttpResponse("hola!!!!!!")
    return render(request,'web/index.html',context)
    
def itinerary(request):
    cities_list = city.objects.order_by('name')
    types_list = type_travel.objects.order_by('name')
    budget_list = budget.objects.order_by('name')
    places_list = place.objects.order_by('name')
    context = {'cities_list':cities_list,'places_list':places_list, 'budget_list':budget_list, 'types_list':types_list}
    if request.method == 'POST':
        return render(request, 'web/itinerary.html', context)
    else:
        return render(request,'web/index.html',context)
        
   
    