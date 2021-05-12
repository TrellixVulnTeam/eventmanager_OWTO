"""
Django settings for eventmanager project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from celery.schedules import crontab

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #'jet.dashboard',
    #'jet',
    "grappelli",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "rest_framework",
    # third party
    "crispy_forms",
    "crispy_tailwind",
    "ckeditor",
    "ckeditor_uploader",
    "easy_thumbnails",
    "tailwind",
    "inline_actions",
    "fieldsets_with_inlines",
    "wkhtmltopdf",
    # tailwind theme app
    "fobi_theme",
    # lokale apps
    "events.apps.EventsConfig",
    "users.apps.UsersConfig",
    "moodle.apps.MoodleConfig",
    "bugz.apps.BugzConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "eventmanager.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "events.custom_context_processor.category_renderer",
            ],
        },
    },
]

WSGI_APPLICATION = "eventmanager.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "de"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

STATICFILES_DIRS = [
    os.path.join(PROJECT_PATH, "static"),
]

# Media files (Images)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Crsipy forms

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"


# Ckeditor config
CKEDITOR_JQUERY_URL = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"

CKEDITOR_UPLOAD_PATH = "event-details/"
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": None,
    },
    "short": {
        "toolbar": "Short",
        "height": 100,
        "toolbar_Short": [
            [
                "Bold",
                "Italic",
                "Link",
                "Unlink",
                "NumberedList",
                "BulletedList",
            ],
            ["FontSize"],
            ["TextColor", "BGColor"],
        ],
    },
}


# easy thumbnails
THUMBNAIL_ALIASES = {
    "": {
        "logo": {"size": (130, 130), "crop": True},
    },
}

# CELERY STUFF
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Europe/Berlin"
CELERY_BEAT_SCHEDULE = {
    # Executes every minute
    "get_courses_from_moodle_every_minute": {
        "task": "events.tasks.get_courses_from_moodle",
        "schedule": crontab(minute="*/1"),
    },
    "get_and_save_courses_from_moodle_every_minute": {
        "task": "events.tasks.get_and_save_courses_from_moodle",
        "schedule": crontab(minute="*/1"),
    },
}

# Tailwind css
TAILWIND_APP_NAME = "fobi_theme"

# for JET WORKING PROPERLY
X_FRAME_OPTIONS = "SAMEORIGIN"

# GRAPPELLI setting
GRAPPELLI_ADMIN_TITLE = "FOBI Eventmanager"


# REST FRAMEWORK
# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }
