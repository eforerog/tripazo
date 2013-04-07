# Create your views here.
from array import array
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson
from web.models import city
from web.models import type_travel
from web.models import place
from web.models import budget
from datetime import datetime

def index(request):
    cities_list = city.objects.order_by('name')
    types_list = type_travel.objects.order_by('name')
    budget_list = budget.objects.order_by('name')
    context = {'cities_list':cities_list, 'types_list':types_list, 'budget_list':budget_list}
    #return HttpResponse("hola!!!!!!")
    return render(request,'web/index.html',context)
    
def itinerary(request):
    month_list = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUNE', 'JULY', 'AUG', 'SEPT', 'OCT','NOV', 'DEC']
    cities_list = city.objects.order_by('name')
    types_list = type_travel.objects.order_by('name')
    budget_list = budget.objects.order_by('name')
    if request.method == 'POST':
        city_id = request.POST.get('city','')
        from_date = datetime.strptime(request.POST.get('from',''),'%d-%m-%Y')
        to_date = datetime.strptime(request.POST.get('to',''),'%d-%m-%Y')
        date_sub = to_date - from_date
        date_sub_days = range(1, date_sub.days+2)
        date_sub_days_max = date_sub.days
        month_from = month_list[from_date.month-1]
        month_to = month_list[to_date.month-1]
        type_travel_id = request.POST.getlist('type_travel')
        
        places_list = place.objects.order_by('name')[:5*(date_sub_days_max+1)]
        _counter_col = 0
        _counter_row = 0
        place_array = []
        place_array.append([])
        for place_for in places_list:
            if _counter_col < 5:
                place_array[_counter_row].append(place_for)
                _counter_col += 1
            else:
                _counter_col = 1
                _counter_row += 1
                place_array.append([])
                place_array[_counter_row].append(place_for)
            
        
        context = {'type_travel_id': type_travel_id, 'cities_list':cities_list,'places_list':place_array, 'budget_list':budget_list, 'types_list':types_list, 'date_sub_days':date_sub_days, 'from_date': from_date, 'to_date':to_date, 'month_from':month_from, 'month_to':month_to, 'date_sub_days_max': date_sub_days_max}
        return render(request, 'web/itinerary.html', context)
    else:
        context = {'cities_list':cities_list,'places_list':places_list, 'budget_list':budget_list, 'types_list':types_list}
        return render(request,'web/index.html',context)
        
   
def json_detail(request):
    details = []
    if request.method == 'GET':
        place_id = request.GET.get('place_id','')
        place_data = place.objects.get(id=place_id)
        details.append({'latitude': str(place_data.latitude), 
                    'longitude': str(place_data.longitude) , 
                    'city': place_data.city,
                    'name': place_data.name,
                    'photo_url1': place_data.photo_url1,
                    'reviews': place_data.reviews,
                    'address': place_data.address,
                    'telephone': place_data.telephone,
                    'website': place_data.website})
    #for co in place_data:
        
    json_data = simplejson.dumps(details)
    return HttpResponse(
        json_data, mimetype="application/json" 
    )
        