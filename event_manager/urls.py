from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),  # Zakładając, że masz URL-e aplikacji events
    path('', include('events.urls')),  # Dodaj tę linię, żeby / kierowało na events (lub inną stronę)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
