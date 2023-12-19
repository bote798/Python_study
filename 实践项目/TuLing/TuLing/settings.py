"""
Django settings for TuLing project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# 将apps文件夹配置到 django 环境中
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x6cg5_1an#-@)$&ya_06f=ic)^6l=jqyyczcy$zct*$-kow4w6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 注册请求白名单
    'corsheaders',
    # 更规范的注册app,使其能够在admin后台显示
    'users.apps.UsersConfig',
    'verification.apps.VerificationConfig'

]

MIDDLEWARE = [
    # CorsMiddleware应该放在尽可能前的位置，尤其是在任何可以生成响应的中间件之前
    # 例如 DjangoCommonMiddleware，如果不在此之前，它将无法将 CORS 标头添加到这些响应中。
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TuLing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'TuLing.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tuling',
        'USER': 'root',
        'PASSWORD': '123456',
        'PORT': 3306,
        'HOST': '127.0.0.1'
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# redis-session 配置
CACHES = {
    # 预留(库: 0)
    "default": {  # 默认
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # session(session信息存储)(库: 1)
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # session(图片验证码信息存储)(库: 2)
    "image_code": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
# 引擎
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 使用的session配置
SESSION_CACHE_ALIAS = "session"

# 日志器配置
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,  # 是否警用已经存在的日志器
    "formatters": {  # 日志信息现实的格式
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "filters": {  # 对日志进行过滤
        # "special": {
        #     "()": "project.logging.SpecialFilter",
        #     "foo": "bar",
        # },

        # 在debug=True时生效
        "require_debug_true": {  # django在debug模式下输出日志
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {  # 日志处理方法
        "console": {  # 向终端中发送日志
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        # "mail_admins": {  # 向管理员的邮箱发送重大错误
        #     "level": "ERROR",
        #     "class": "django.utils.log.AdminEmailHandler",
        #     "filters": ["special"],
        # },
        "file": {  # 向文件中输出日志
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/TuLing.log"),  # 日志文件的位置
            "maxBytes": 300 * 1024 * 1024,
            "backupCount": 10,
            "formatter": "verbose"
        },
    },
    "loggers": {  # 日志器
        "django": {  # 定义了一个名为django的日志器
            "handlers": ["console", "file"],  # 可以同时向终端与文件中输出日志
            "propagate": True,  # 是否继续传递日志信息
            "level": "INFO"  # 日志器接受的最低日志等级
        },
        # "django.request": {
        #     "handlers": ["mail_admins"],
        #     "level": "ERROR",
        #     "propagate": False,
        # },
        # "myproject.custom": {
        #     "handlers": ["console", "mail_admins"],
        #     "level": "INFO",
        #     "filters": ["special"],
        # },
    },
}
# 用户模型类的覆盖
'''
因为django 默认的用户表关联了用户组表和用户权限表

有两个user模型 同时继承了AbstractUser。
所以这里需要指定模型,指定后,未指定的模型就不会使用了
'''
AUTH_USER_MODEL = 'users.User'

# CORS 请求白名单
# 使用之前记得安装cors模块（pip install django-cors-headers）
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    # 测试记得 python manage.py runserver 127.0.0.1:8080
    # 这样开放8080端口才能使用下列进行访问
    'http://127.0.0.1:8080',
    'http://localhost:8080',
)

# 指明在跨域访问中，后端是否支持对cookie的操作。
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie
