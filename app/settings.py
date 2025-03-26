# from pathlib import Path
# from decouple import config
# import os

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config('SECRET_KEY')

# # SECURITY WARNING: don't run with debug turned on in production!
# # DEBUG = True faz com que o Django mostre a página de erro com detalhes
# # cast=bool converte a string para boolean
# DEBUG = config('DEBUG', default=False, cast=bool)

# # para permitir todos os hosts que estão conectados à minha rede.
# ALLOWED_HOSTS = ["*"]
# # tem que colocar uma regra de entrada no firewall
# # py manage.py runserver 0.0.0.0:Porta    - o IP é o do meu pc


# # Application definition

# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",

#     'django_htmx', # HTMX
#     'widget_tweaks', # Widget Tweaks

#     "autenticacao",
#     "clientes",
#     "configuracoes",
#     "contratos",
#     "emails",
#     "empresas",
#     "eventos",
#     "noticias",
#     "palavras_chave",
#     "relatorios",
#     "site_cliente",
#     "veiculos",
# ]

# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "app.middleware.cliente_middleware.ClienteSelecionadoMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     'django_htmx.middleware.HtmxMiddleware', # Middleware do HTMX
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]

# ROOT_URLCONF = "app.urls"

# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": ["app/templates"],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#                 "app.context_processors.cliente_selecionado", # 👈 
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = "app.wsgi.application"


# # Database
# # https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": config("DB_ENGINE"),
#         "NAME": config("DB_NAME"),
#         "USER": config("DB_USER"),
#         "PASSWORD": config("DB_PASSWORD"),
#         "HOST": config("DB_HOST"),
#         "PORT": config("DB_PORT"),
#         "OPTIONS": {
#             "driver": config("DB_DRIVER"),
#             "trustServerCertificate": config("DB_TRUSTED_CERT"),
#             "extra_params": config("DB_EXTRA_PARAMS"),
#         },
#     }
# }


# # Password validation
# # https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = "pt-br"

# TIME_ZONE = "America/Sao_Paulo"

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.0/howto/static-files/

# STATIC_URL = "static/"
# STATICFILES_DIRS = [BASE_DIR / "static"]
# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# # Default primary key field type
# # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# # proteções de segurança
# SECURE_BROWSER_XSS_FILTER = True
# X_FRAME_OPTIONS = "DENY"
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True



from pathlib import Path
from decouple import config
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ⚠️ Deixe DEBUG como True durante os testes públicos (mostra erros detalhados)
DEBUG = config('DEBUG', default=True, cast=bool)

# ✅ Permite qualquer host acessar (qualquer IP ou domínio)
ALLOWED_HOSTS = ['*']

# 🔑 Chave secreta
SECRET_KEY = config('SECRET_KEY')

# Aplicativos instalados
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'django_htmx',
    'widget_tweaks',

    "autenticacao",
    "clientes",
    "configuracoes",
    "contratos",
    "emails",
    "empresas",
    "eventos",
    "noticias",
    "palavras_chave",
    "relatorios",
    "site_cliente",
    "veiculos",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "app.middleware.cliente_middleware.ClienteSelecionadoMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["app/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "app.context_processors.cliente_selecionado",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
        "OPTIONS": {
            "driver": config("DB_DRIVER"),
            "trustServerCertificate": config("DB_TRUSTED_CERT"),
            "extra_params": config("DB_EXTRA_PARAMS"),
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 🚫 Desativa segurança HTTPS para permitir acesso público via HTTP
CSRF_COOKIE_SECURE = False  # ❗ Permite envio de formulários sem HTTPS
SESSION_COOKIE_SECURE = False  # ❗ Permite manter sessões sem HTTPS

# ⚠️ Manter estas duas ativa
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
