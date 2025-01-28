from django import forms
from .models import Event, Category, Location, Ticket

# Formularz dla Event
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'category']  # lub inne pola

# Formularz dla Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

# Formularz dla Location
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'address', 'city']

# Formularz dla Ticket
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['event', 'price', 'available']
