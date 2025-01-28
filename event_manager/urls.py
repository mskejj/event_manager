# filepath: /Users/dawid/Desktop/apliakcje/event_manager/event_manager/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel admina
    path('', include('events.urls')),  # Ścieżki URL z aplikacji 'events'
]
