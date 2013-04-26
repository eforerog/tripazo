# Create your views here.
from array import array
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson
from web.models import city
from web.models import type_travel
from web.models import type
from web.models import place
from web.models import place_relevance
from web.models import budget
from datetime import datetime
from django.db.models import Q
import math
from decimal import Decimal 

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
        city_id = request.POST.get('city_id','')
        from_date = datetime.strptime(request.POST.get('from',''),'%d-%m-%Y')
        to_date = datetime.strptime(request.POST.get('to',''),'%d-%m-%Y')
        date_sub = to_date - from_date
        date_sub_days = range(1, date_sub.days+2)
        date_sub_days_max = date_sub.days
        month_from = month_list[from_date.month-1]
        month_to = month_list[to_date.month-1]
        type_travel_id = request.POST.getlist('type_travel')
        budget_name=request.POST.get('budget')
        
        ##places_list is an array storing 5*duration-of-the-trip-(in days) activities.  
        #places_list = place.objects.order_by('name')[:5*(date_sub_days_max+1)]
        
        #smart algorithm
        #places_list = place.objects.filter(type='bowling_alley')[:5] 
        #places_list = place.objects.filter(type="bowling_alley").order_by('-rating')[:10]
             
        #assigning price target to traveler budgets ("fuzzifier!") 
        if budget_name=="Saver": #saver
            target_price=Decimal(1)
        elif budget_name=="On budget":#on budget
            target_price=Decimal(2)
        else:    #luxury/baller
            target_price=Decimal(3.5)  
        
         
        #my_traveler_type=[10,9,2]
        my_traveler_type=type_travel_id
        
        #Select the traveler profile 
        x = [ ]
        for k in range(len(my_traveler_type)):
        
            y = type.objects.filter(type_travel_id=my_traveler_type[k])
            #Select all activities from all google types related to the traveler profile
            for i in range(len(y)):  #i hold the google type index
                z = place.objects.filter(type=y[i].name) #select all objects with the i type 
                for j in range(len(z)):
                    # Set up price_bonus , it must be 0 if object has no prive_level info.  
                    if z[j].price_level == 0: #When importing data Edgar set price_level to 0 when no data was avaialble
                        z[j].price_bonus=Decimal(0)
                    else:
                        z[j].price_bonus=Decimal((-math.fabs(target_price-z[j].price_level))+1)
                    #try to setup relavance. use specific relevance if extis, if not, use google type revelevan
                    try:
                        myobject=place_relevance.objects.filter(place_id=z[j].id)
                        z[j].relevance=myobject[0].weight
                    except IndexError:
                        myobject=type.objects.filter(Q(name=y[i].name)&Q(type_travel_id=my_traveler_type[k]))
                        z[j].relevance=myobject[0].weight
                    
                    #if rating is None, set it to 0 
                    if z[j].rating is None:
                        z[j].rating=Decimal(0)
                        
                    z[j].total_relevance = z[j].price_bonus + z[j].relevance
                    z[j].ranking = (z[j].total_relevance + z[j].rating)/2
                    
                    #concatenate arrays to have all google types resutls in the same array x 
                x.extend(z)
        #sort results by relevance    
        w=sorted(x, key=lambda place: -place.ranking)         
        places_list=w[:5*(date_sub_days_max+1)]
        
        

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
        