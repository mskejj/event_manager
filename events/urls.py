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
from .views import TicketDeleteView

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    # Inne ścieżki URL
    path('event/new/', views.event_create, name='event_create'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('summary/', views.event_summary, name='event_summary'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/new/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('locations/', views.location_list, name='location_list'),
    path('locations/new/', views.location_create, name='location_create'),
    path('locations/<int:pk>/edit/', views.location_edit, name='location_edit'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/new/', views.ticket_create, name='ticket_create'),
    path('tickets/<int:pk>/edit/', views.ticket_edit, name='ticket_edit'),
    path('tickets/<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
]

