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
    "vinculos_clientes_noticias",  # Novo app para vincular notícias a clientes e categorias
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
