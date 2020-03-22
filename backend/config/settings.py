import os
from datetime import timedelta


def __find_manage_py_directory():
    """Using path of module that imported _this_ module to search for manage.py"""
    import inspect
    import os

    # get paths of modules from callstack
    frame_paths = [
        f[1] for f in inspect.getouterframes(inspect.currentframe()) if f[3] == "<module>"
    ]
    # first entry is _this_ module, second entry is the module that imported _this_ module
    imported_from_path = os.path.abspath(frame_paths[1])
    test_dir = os.path.dirname(imported_from_path)
    while True:
        manage_py = os.path.join(test_dir, "manage.py")
        if os.path.isfile(manage_py):
            return test_dir
        test_dir = os.path.normpath(os.path.join(test_dir, "..")) if test_dir != os.sep else ""
        if not test_dir:
            return os.path.abspath(".")  # assuming current working directory


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = __find_manage_py_directory()
ROOT_URLCONF = "pet_help.urls"
WSGI_APPLICATION = "config.wsgi.application"
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True  # FIXME: replace with CORS_ORIGIN_WHITELIST = [frontend-host]

AUTH_USER_MODEL = 'pet_help.User'

# from env
DEBUG = os.getenv("DJANGO_DEBUG", "false")
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "+2d*2u+s1b=sz9tjv0cacr!bs9+-^)5g+bp0do@ltmfc^1hs!^")
MAP_QUEST_API_KEY = os.getenv("MAP_QUEST_API_KEY", "")
MAP_QUEST_GEOCODING_URL = "https://www.mapquestapi.com/geocoding/v1/address"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "health_check",
    "health_check.db",
    "corsheaders",
    "pet_help",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework_simplejwt.authentication.JWTAuthentication'],
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite')
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=12),
    'ROTATE_REFRESH_TOKENS': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': os.getenv("JWT_SIGNING_KEY", SECRET_KEY),
}
