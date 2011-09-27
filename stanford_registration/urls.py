from django.conf.urls import patterns, include, url


urlpatterns = patterns('stanford_registration.views',
    url(r'login/$', 'login'),
    url(r'authenticate/$', 'authenticate'),
)