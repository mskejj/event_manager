from django import forms
from .models import Event, Category, Location, Ticket

# Formularz dla Event
class EventForm(forms.ModelForm):
    image = forms.ImageField(required=False)  # Dodane pole

    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'location', 'category']  # Usunięte pole image z modelu

# Formularz dla Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

# Formularz dla Location
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'city', 'address']

# Formularz dla Ticket
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['event', 'available', 'price']
