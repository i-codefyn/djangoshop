"""codefyn_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.apps import apps
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

# from SRC.Oscar import views


urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("admin/", admin.site.urls),
    # path("", include("home.urls"), name="index"),
    path("shop/", include(apps.get_app_config("oscar").urls[0])),
    path("dashboard/", apps.get_app_config("catalogue_dashboard").urls),
    path("accounts/", include("allauth.urls")),
    path("checkout/rzpay", apps.get_app_config("rzpay").urls),
    path("", apps.get_app_config("home").urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
