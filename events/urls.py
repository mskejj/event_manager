from django.contrib import admin
from django.urls import path, include  # Dodaj include
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel admina
    path('', include('events.urls')),  # Ścieżki URL z aplikacji 'events'
]

# filepath: /Users/dawid/Desktop/apliakcje/event_manager/events/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),  # Domyślna strona główna
    path('events/', views.event_list, name='event_list'),
    path('event/<int:id>/', views.event_detail, name='event_detail'),
    path('events/new/', views.event_create, name='event_create'),  # Nowa ścieżka URL
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('locations/', views.location_list, name='location_list'),
    path('locations/<int:pk>/', views.location_detail, name='location_detail'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/<int:pk>/', views.ticket_detail, name='ticket_detail'),
    path('events/this_month/', views.events_per_month, name='events_per_month'),  # Nowa ścieżka URL
]

