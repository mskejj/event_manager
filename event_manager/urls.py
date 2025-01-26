from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel admina
    path('', views.event_list, name='event_list'),  # Strona główna z listą wydarzeń
    path('event/<int:pk>/', views.event_detail, name='event_detail'),  # Szczegóły wydarzenia
    path('event/new/', views.event_create, name='event_create'),  # Dodawanie nowego wydarzenia
    path('event/edit/<int:pk>/', views.event_edit, name='event_edit'),  # Edytowanie wydarzenia
    path('event/delete/<int:pk>/', views.event_delete, name='event_delete'),  # Usuwanie wydarzenia
]
