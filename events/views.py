from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm

# Widok listy wydarzeń
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

# Widok szczegółów pojedynczego wydarzenia
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})

# Widok tworzenia nowego wydarzenia
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})

# Widok edycji istniejącego wydarzenia
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'event_form.html', {'form': form})

# Widok usuwania wydarzenia
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'event_confirm_delete.html', {'event': event})

