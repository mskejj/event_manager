from pathlib import Path
import os  # Importujemy moduł os

# Budowanie ścieżek wewnątrz projektu, np. BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Ustawienia do szybkiego startu - nieodpowiednie do produkcji
# Zobacz: https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# OSTROŻNOŚĆ: Trzymaj klucz sekretu w tajemnicy w środowisku produkcyjnym!
SECRET_KEY = 'django-insecure-ejw&ei(%5rq@14g=f(xga4ver5z4!@v7rrt!!n1lf^^d$54m+='

# OSTROŻNOŚĆ: Nie uruchamiaj aplikacji z włączonym DEBUG w produkcji!
DEBUG = True

ALLOWED_HOSTS = []  # Lista dozwolonych hostów (pusta w trybie deweloperskim)

# Definicja aplikacji

INSTALLED_APPS = [
    'django.contrib.admin',  # Panel administratora
    'django.contrib.auth',  # Aplikacja do zarządzania użytkownikami
    'django.contrib.contenttypes',  # Aplikacja do zarządzania typami danych
    'django.contrib.sessions',  # Aplikacja do zarządzania sesjami
    'django.contrib.messages',  # Aplikacja do obsługi wiadomości
    'django.contrib.staticfiles',  # Aplikacja do obsługi plików statycznych
    'events',  # Dodajemy naszą aplikację 'events'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Middleware do bezpieczeństwa
    'django.contrib.sessions.middleware.SessionMiddleware',  # Middleware do sesji
    'django.middleware.common.CommonMiddleware',  # Middleware do ogólnych operacji
    'django.middleware.csrf.CsrfViewMiddleware',  # Middleware do ochrony przed atakami CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Middleware do autentykacji
    'django.contrib.messages.middleware.MessageMiddleware',  # Middleware do wiadomości
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Middleware do ochrony przed clickjacking
]

ROOT_URLCONF = 'event_manager.urls'  # Konfiguracja URL głównej aplikacji

TEMPLATES = [  # Poprawiona literówka, teraz prawidłowo pisane 'TEMPLATES'
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Backend szablonów
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Ścieżka do folderu z szablonami
        'APP_DIRS': True,  # Automatyczne szukanie szablonów w aplikacjach
        'OPTIONS': {
            'context_processors': [  # Przetworniki kontekstu
                'django.template.context_processors.debug',  # Przetwornik debug
                'django.template.context_processors.request',  # Przetwornik żądań
                'django.contrib.auth.context_processors.auth',  # Przetwornik autentykacji
                'django.contrib.messages.context_processors.messages',  # Przetwornik wiadomości
            ],
        },
    },
]

WSGI_APPLICATION = 'event_manager.wsgi.application'  # Konfiguracja aplikacji WSGI

# Baza danych
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Silnik bazy danych
        'NAME': BASE_DIR / 'db.sqlite3',  # Ścieżka do pliku bazy danych
    }
}

# Walidacja haseł
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Walidator podobieństwa atrybutów
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Walidator minimalnej długości hasła
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Walidator powszechnych haseł
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Walidator haseł numerycznych
    },
]

# Międzynarodowe ustawienia
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pl'  # Zmieniamy na polski

TIME_ZONE = 'Europe/Warsaw'  # Zmieniamy na strefę czasową Polski

USE_I18N = True  # Włączamy międzynarodowe ustawienia

USE_TZ = True  # Włączamy strefy czasowe

# Pliki statyczne (CSS, JavaScript, obrazy)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'  # URL dla plików statycznych
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Dodajemy ścieżkę do katalogu z plikami statycznymi
STATIC_ROOT = BASE_DIR / "staticfiles"  # Ścieżka do katalogu dla skompilowanych plików statycznych

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Domyślny typ klucza głównego
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Ustawiamy domyślny typ pola auto dla klucza głównego
