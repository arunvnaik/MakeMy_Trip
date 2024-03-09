# admin.py

from django.contrib import admin
from trip_app.models import Customer, Location, Cost

admin.site.register(Customer)
admin.site.register(Location)
admin.site.register(Cost)



# Register your models here.
