from django.conf import settings
from django.conf.urls.defaults import *
from social_auth.models import PROVIDERS


urlpatterns = patterns('social_auth.views',
    url(r'^logout/$', 'logout', name='auth_logout'),
    url(r'^status/$', 'status', name='auth_status'),
    url(r'^submit/$', 'submit', name='auth_submit'),
)

for provider in PROVIDERS:
    urlpatterns += patterns('social_auth.views',
        url(r'^%s/$' % provider, provider, name='auth_%s' % provider),
        url(r'^logout/%s/$' % provider,
            'logout',
            {'provider': provider},
            name='auth_logout_%s' % provider),
    )

if getattr(settings, 'SOCIAL_AUTH_DEBUG', False):
    urlpatterns += patterns('social_auth.views',
        url(r'^test/(?P<u_id>[\d]+)$', 'test', name='auth_test'),
    )
