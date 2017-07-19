"""
Definition of urls for MySite.
"""

from django.conf.urls import include, url
from store.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', home, name='home' ),
    url(r'^(?P<skunum>[0-9]+)/$', itemdetail, name='itemdetails'),
    url(r'^(?i)register/$', register ,name='registerform'),
    url(r'^(?i)cart/$',cart ,name='cart'),
    url(r'^tocart/$', tocart ,name='tocart'),
    url(r'^user/$',profile,name='user'),
    url(r'^catgory/(?P<category>.*)',catgories,name='categories')


]
