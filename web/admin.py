from django.contrib import admin
from web.models import city
from web.models import type_travel
from web.models import type
from web.models import place
from web.models import place_relevance
from web.models import budget
from web.models import budget_tripazo

class budget_tripazoAdmin(admin.ModelAdmin):
    list_display = ('budget', 'google_price_level')

class place_relevanceAdmin(admin.ModelAdmin):
    list_display = ('type_travel', 'place', 'weight')
    list_filter = ['type_travel']
    search_fields = ['place']

class placeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'rating', 'city', 'country')
    list_filter = ['type']
    search_fields = ['name']   

class typeAdmin(admin.ModelAdmin):
    list_display = ('type_travel', 'name', 'weight')
    list_filter = ['type_travel']
    search_fields = ['name']  
         
admin.site.register(city)
admin.site.register(type_travel)
admin.site.register(type, typeAdmin)
admin.site.register(place, placeAdmin)
admin.site.register(place_relevance, place_relevanceAdmin)
admin.site.register(budget)
admin.site.register(budget_tripazo, budget_tripazoAdmin)
