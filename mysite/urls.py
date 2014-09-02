from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^nss/', include('nss_admin.urls')),
    url(r'^samba_admin/', include('samba_admin.urls')),
    url(r'^dhcp_admin/', include('dhcp_admin.urls')),
#    url(r'^schedule/', include('school_sched.urls')),
#    url(r'^agenda/', include('schoolagenda.urls')),
)


handler404 = 'django.views.defaults.page_not_found'
handler500 = 'django.views.defaults.server_error'

# enable serving static files on debugging server
if settings.SERVE_STATICS:
    urlpatterns += patterns('', (
        r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
        'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }
    ), )

    urlpatterns += staticfiles_urlpatterns()
