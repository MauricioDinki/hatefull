#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Production settings
- Run in production mode
- Use Amazon's S3 for storing static files
"""

from .base import *  # noqa

import six

# DEBUG
# -----------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=False)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SITE CONFIGURATION
# -----------------------------------------------------------------------------
ALLOWED_HOSTS = ["*"]

# DATABASE
# -----------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'STORAGE_ENGINE': 'MyISAM / INNODB / ETC',
        'NAME': 'hatefull',
        'USER': 'root',
        'PASSWORD': 'hatefull',
        'HOST': '',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
            "init_command": "SET foreign_key_checks = 0;",
        },
    }
}

# STORAGE CONFIGURATION
# -----------------------------------------------------------------------------
INSTALLED_APPS += (
    'storages',
)

# STATIC CONFIGURATION
# -----------------------------------------------------------------------------

# Amazon s3 configuration
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")

AWS_EXPIRY = 60 * 60 * 24 * 7

AWS_HEADERS = {
    'Cache-Control': six.b('max-age=%d, s-maxage=%d, must-revalidate' % (
        AWS_EXPIRY, AWS_EXPIRY))
}

# static

STATIC_URL = "https://%s/" % env("AWS_BUCKET_URL", None)

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# MEDIA CONFIGURATION
# -----------------------------------------------------------------------------
MEDIA_ROOT = str(PROJECT_DIR('media'))

MEDIA_URL = '/media/'
