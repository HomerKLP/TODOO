DJANGO_MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SIDE_MIDDLEWARE = (
    'corsheaders.middleware.CorsMiddleware',
    'silk.middleware.SilkyMiddleware',
)

BEFORE = DJANGO_MIDDLEWARE[:3]
AFTER = DJANGO_MIDDLEWARE[3:]
DEFAULT_MIDDLEWARE = BEFORE + SIDE_MIDDLEWARE + AFTER
