from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import patterns, include
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import internals.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

dajaxice_autodiscover()

urlpatterns = patterns('',
    url(r'^register\.html$', internals.views.register, name='register'),
    url(r'^login\.html$', internals.views.login, name='login'),
    url(r'^index\.html$|^$', internals.views.index, name='index'),
    url(r'^test\.html$', internals.views.test, name='test'),
    url(r'^logout\.html$|^$', internals.views.logout, name='logout'),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls'))
    # Examples:
    # url(r'^$', 'adoptaschool.views.home', name='home'),
    # url(r'^adoptaschool/', include('adoptaschool.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
