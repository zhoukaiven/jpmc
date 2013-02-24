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
    url(r'^multimedia\.html$|^$', internals.views.multimedia, name='multimedia'),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^logout\.html$|^$', internals.views.logout, name='logout'),
    url(r'^schoolDesigner\.html$|^$', internals.views.school_designer, name='school_designer'),
    url(r'^controlPanel\.html$|^$', internals.views.control_panel, name='control_panel'),
    url(r'^groupHomePage\.html$|^$', internals.views.group_home_page, name='groupHomePage'),                   
    # Examples:
    # url(r'^$', 'adoptaschool.views.home', name='home'),
    # url(r'^adoptaschool/', include('adoptaschool.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
