"""
Django settings for codefyn_shop project.

Generated by 'django-admin startproject' using Django 2.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()
from oscar.defaults import *
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

# Shop name
OSCAR_SHOP_NAME = "Codefyn"
OSCAR_SHOP_TAGLINE="Fast delivery"
location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", x)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

DEBUG = int(env("DEBUG", default=0))
# DEBUG = True

from django.core.management.utils import get_random_secret_key

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-jpjhb)$cjy4k=j#x76x%d90a4)e(1$zs)p!rj7lw#tm_r$-wzd'
SECRET_KEY = get_random_secret_key()

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ["myshop.codefyn.com"]


# Application definition

INSTALLED_APPS = [
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.flatpages",
    "home.apps.HomeConfig",
    # "oscar",
    # "oscar.apps.customer.notifications",
    "oscar.config.Shop",
    "oscar.apps.analytics.apps.AnalyticsConfig",
    "oscar.apps.address.apps.AddressConfig",
    "oscar.apps.shipping.apps.ShippingConfig",
    # "oscar.apps.checkout.apps.CheckoutConfig",
    "new_checkout.apps.CheckoutConfig",
    "new_catalogue.apps.CatalogueConfig",
    "new_catalogue.reviews.apps.CatalogueReviewsConfig",
    # "oscar.apps.catalogue.apps.CatalogueConfig",
    # "oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig",
    "oscar.apps.communication.apps.CommunicationConfig",
    "oscar.apps.partner.apps.PartnerConfig",
    "oscar.apps.basket.apps.BasketConfig",
    "oscar.apps.payment.apps.PaymentConfig",
    "oscar.apps.offer.apps.OfferConfig",
    "oscar.apps.order.apps.OrderConfig",
    "oscar.apps.customer.apps.CustomerConfig",
    "oscar.apps.search.apps.SearchConfig",
    "oscar.apps.voucher.apps.VoucherConfig",
    "oscar.apps.wishlists.apps.WishlistsConfig",
    "oscar.apps.dashboard.apps.DashboardConfig",
    "oscar.apps.dashboard.reports.apps.ReportsDashboardConfig",
    "oscar.apps.dashboard.users.apps.UsersDashboardConfig",
    "oscar.apps.dashboard.orders.apps.OrdersDashboardConfig",
    "oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig",
    "oscar.apps.dashboard.offers.apps.OffersDashboardConfig",
    "oscar.apps.dashboard.partners.apps.PartnersDashboardConfig",
    "oscar.apps.dashboard.pages.apps.PagesDashboardConfig",
    "oscar.apps.dashboard.ranges.apps.RangesDashboardConfig",
    "oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig",
    "oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig",
    "oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig",
    "oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig",
    # 3rd-party apps that oscar depends on
    "widget_tweaks",
    "haystack",
    "treebeard",
    "sorl.thumbnail",
    "django_tables2",
    "allauth",  # new
    "allauth.account",  # new
    "allauth.socialaccount",  # new
    "allauth.socialaccount.providers.facebook",  # new
    "allauth.socialaccount.providers.google",  # new
    "send",
    # "pages",
    "multiselectfield",
    "rzpay.apps.RzpayConfig",
    "captcha",
 
]

SITE_ID = 1

OSCAR_PAYMENT_METHODS = (("Rzpay", ("Rozar Pay")),)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "oscar.apps.basket.middleware.BasketMiddleware",
]
LOGIN_REDIRECT_URL = "/"

AUTHENTICATION_BACKENDS = (
    "oscar.apps.customer.auth_backends.EmailBackend",
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
ROOT_URLCONF = "codefyn_shop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [location("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "oscar.apps.search.context_processors.search_form",
                "oscar.apps.checkout.context_processors.checkout",
                # "oscar.apps.customer.notifications.context_processors.notifications",
                "oscar.core.context_processors.metadata",
                "home.context_processors.wishlists",
            ],
            # ! New Line
            "libraries": {
                "products": "templatetags.products",
                "history": "templatetags.history",
            },
        },
    },
]
STATIC_ROOT = "/home/uzmylats/public_html/myshop.codefyn.com/static"
STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
    os.path.join(BASE_DIR, "/home/uzmylats/public_html/myshop.codefyn.com/media"),
]  # new
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # new
# mdeidia setting
MEDIA_URL = "/media/"  # new
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")  # new
MEDIA_ROOT = '/home/uzmylats/public_html/myshop.codefyn.com/media' 
STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


WSGI_APPLICATION = "codefyn_shop.wsgi.application"

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.simple_backend.SimpleEngine",
    },
}
RECAPTCHA_PUBLIC_KEY = env("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = env("RECAPTCHA_PRIVATE_KEY")
RAZORPAY_VENDOR_LOGO = "https://via.placeholder.com/150x150"
RAZORPAY_THEME_COLOR = "#F37254"
RAZORPAY_VENDOR_NAME = "Codefyn"
RAZORPAY_PUBLIC_KEY = env("RAZORPAY_PUBLIC_KEY")
RAZORPAY_SECRET_KEY = env("RAZORPAY_SECRET_KEY")
RAZORPAY_API_KEY = RAZORPAY_PUBLIC_KEY
# PAYMENT_VARIANTS = {
#     "razorpay": (
#         "django_payments_razorpay.RazorPayProvider",
#         {"public_key": "RAZORPAY_PUBLIC_KEY", "secret_key": "RAZORPAY_SECRET_KEY"},
#     )
# }

from django.utils.translation import ugettext_lazy as _

# Payments
# OSCAR_DASHBOARD_NAVIGATION.append(
#     {
#         "label": _("Rzorpay"),
#         "icon": "icon-globe",
#         "children": [
#             {
#                 "label": _("Rzpay transactions"),
#                 "url_name": "rzpay:razorpay-direct-payment",
#             },
#         ],
#     }
# )
CHECKOUT_PAYMENT_CHOICES = [("razorpay", "RazorPay")]
# Provide a lists of languages which your site supports.
USE_MODELTRANSLATION = True

LANGUAGES = (("en", _("English")),)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_URL = "/static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
#     "/var/www/static/",
# ]


# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

LOCALE_PATHS = ("locale",)
# OSCAR CONFIG

OSCAR_HOMEPAGE = reverse_lazy("home:index")


# Settings for sending email #

MAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_SSL = False

# ------------------------------------ #


# CURRENCY CONFIG

OSCAR_DEFAULT_CURRENCY = "INR"

OSCAR_CURRENCY_FORMAT = {
    "INR": {
        "currency_digits": False,
        "format_type": "accounting",
        "format": "\u20B9,##0.000",
    }
}


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

import pymysql

pymysql.install_as_MySQLdb()
DATABASES = {
    "default": {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        "ENGINE": env("ENGINE"),  # <-- UPDATED line
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD":env("DATABASE_PASS"),
        "HOST": env("DATABASE_HOST"),
        "PORT": env("DATABASE_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"