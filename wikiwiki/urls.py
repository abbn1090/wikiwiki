from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.conf.urls.defaults import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wikiwiki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('wiki.urls')),
    url(r'^markdown/', include('django_markdown.urls')),
   # url(r'^pastebin/', include('pastebin.urls')),
    #url(r'^blog/', include('blog.urls')),
)



