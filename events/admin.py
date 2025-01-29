from django.contrib import admin
from .models import Category, Event, Location, Ticket

# Zarejestruj swoje modele tutaj.
admin.site.register(Category)
# admin.site.register(Organizer)
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Ticket)
