"""
Definition of urls for MySite.
"""

from django.conf.urls import include, url
from MySite.views import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    # Examples:

    url(r'^$' ,home, name="portfolio"),
    url(r'^(?i)store/',include("store.urls",namespace="main_store", app_name="store")),

    # url(r'^$', MySite.views.home, name='home'),
    # url(r'^MySite/', include('MySite.MySite.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls))
]
