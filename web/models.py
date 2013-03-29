from django.db import models

# Create your models here.
class city(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=12, decimal_places=8)
    longitude = models.DecimalField(max_digits=12, decimal_places=8)
    def __unicode__(self):
        return self.name    

class type_travel(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
        
class type(models.Model):
    type_travel = models.ForeignKey(type_travel)
    name = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    def __unicode__(self):
        return self.name
    
class place(models.Model):
    latitude = models.DecimalField(max_digits=12, decimal_places=8)
    longitude = models.DecimalField(max_digits=12, decimal_places=8)
    icon = models.CharField(max_length=500)
    id_google = models.CharField(max_length=1000)
    name = models.CharField(max_length=500)
    photo_url1 = models.CharField(max_length=2000)
    photo_url2 = models.CharField(max_length=2000)
    photo_url3 = models.CharField(max_length=2000)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    reference = models.CharField(max_length=2000)
    opening_hours_0_open = models.DecimalField(max_digits=4, decimal_places=2)
    opening_hours_0_close = models.DecimalField(max_digits=4, decimal_places=2)
    opening_hours_1_open = models.DecimalField(max_digits=4, decimal_places=2)
    opening_hours_1_close = models.DecimalField(max_digits=4, decimal_places=2)
    opening_hours_2_open = models.DecimalField(max_digits=4, decimal_places=2)
    opening_hours_2_close = models.DecimalField(max_digits=4, decimal_places=2)
    opening_hours_3_open = models.DecimalField(max_digits=4, decimal_places=2)
    opening_hours_3_close = models.DecimalField(max_digits=4, decimal_places=2)
    opening_hours_4_open = models.DecimalField(max_digits=4, decimal_places=2)
    opening_hours_4_close = models.DecimalField(max_digits=4, decimal_places=2)
    opening_hours_5_open = models.DecimalField(max_digits=4, decimal_places=2)
    opening_hours_5_close = models.DecimalField(max_digits=4, decimal_places=2)
    opening_hours_6_open = models.DecimalField(max_digits=4, decimal_places=2)
    opening_hours_6_close = models.DecimalField(max_digits=4, decimal_places=2)
    price_level = models.DecimalField(max_digits=4, decimal_places=2)
    reviews = models.CharField(max_length=2000)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    telephone = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
        
class place_relevance(models.Model):
    type_travel = models.ForeignKey(type_travel)
    place = models.ForeignKey(place)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    def __unicode__(self):
        return self.place.name

class budget(models.Model):
    name = models.CharField(max_length=500)
    def __unicode__(self):
        return self.name

class budget_tripazo(models.Model):
    budget = models.ForeignKey(budget)
    google_price_level = models.DecimalField(max_digits=2, decimal_places=0)
    def __unicode__(self):
        return self.budget.name