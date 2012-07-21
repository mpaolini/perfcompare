from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^$', 'main.views.index'),
    # Examples:
    # url(r'^$', 'perfcompare.views.home', name='home'),
    # url(r'^perfcompare/', include('perfcompare.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': './main/static/',
                }),
        )
