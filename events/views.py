from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Category, Location, Ticket
from .forms import EventForm, CategoryForm, LocationForm, TicketForm
from django.urls import reverse_lazy
from django.views.generic import DeleteView

# Widok listy wydarzeń
def event_list(request):
    events = Event.objects.all()  # Pobiera wszystkie wydarzenia z bazy
    return render(request, 'events/event_list.html', {'events': events})

# Widok szczegółów wydarzenia
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)  # Pobiera konkretne wydarzenie
    return render(request, 'events/event_detail.html', {'event': event})

# Widok tworzenia nowego wydarzenia
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

# Widok edycji wydarzenia
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Przekierowanie po zapisaniu
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_edit.html', {'form': form})

# Widok usuwania wydarzenia
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')  # Przekierowanie po usunięciu
    return render(request, 'events/event_confirm_delete.html', {'event': event})

# Widok podsumowania wydarzeń
def event_summary(request):
    events = Event.objects.all()  # Pobierz wszystkie wydarzenia
    return render(request, 'events/event_summary.html', {'events': events})

# Widok listy kategorii
def category_list(request):
    categories = Category.objects.all()  # Pobieramy wszystkie kategorie
    return render(request, 'events/category_list.html', {'categories': categories})

# Widok szczegółów dla Category
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'events/category_detail.html', {'category': category})

# Widok tworzenia nowej kategorii
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'events/category_form.html', {'form': form})

# Widok edycji kategorii
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'events/category_form.html', {'form': form})

# Widok listy lokalizacji
def location_list(request):
    locations = Location.objects.all()  # Pobieramy wszystkie lokalizacje
    return render(request, 'events/location_list.html', {'locations': locations})

# Widok szczegółów dla Location
def location_detail(request, pk):
    location = get_object_or_404(Location, pk=pk)
    return render(request, 'events/location_detail.html', {'location': location})

# Widok tworzenia nowej lokalizacji
def location_create(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm()
    return render(request, 'events/location_form.html', {'form': form})

# Widok edycji lokalizacji
def location_edit(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm(instance=location)
    return render(request, 'events/location_form.html', {'form': form})

# Widok listy biletów
def ticket_list(request):
    tickets = Ticket.objects.all()  # Pobieramy wszystkie bilety
    return render(request, 'events/ticket_list.html', {'tickets': tickets})

# Widok szczegółów dla Ticket
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'events/ticket_detail.html', {'ticket': ticket})

# Widok tworzenia nowego biletu
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'events/ticket_form.html', {'form': form})

# Widok edycji biletu
def ticket_edit(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'events/ticket_form.html', {'form': form})

class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'events/ticket_confirm_delete.html'  # Szablon potwierdzenia usunięcia
    success_url = reverse_lazy('ticket_list')  # Po usunięciu przekierowanie na listę biletów
