from django.conf.urls import patterns, include, url
import internals.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^register\.html$', internals.views.register, name='register'),
    url(r'^login\.html$', internals.views.login, name='login'),
    url(r'^index\.html$|^$', internals.views.index, name='index'),
    url(r'^logout\.html$|^$', internals.views.logout, name='logout'),
    url(r'^schoolDesigner\.html$|^$', internals.views.school_designer, name='school_designer'),
    url(r'^controlPanel\.html$|^$', internals.views.control_panel, name='control_panel'),
    url(r'^groupHomePage\.html$|^$', internals.views.group_home_page, name='groupHomePage'),
    url(r'^multimedia\.html$|^$', internals.views.multimedia, name='multimedia'),
    # Examples:
    # url(r'^$', 'adoptaschool.views.home', name='home'),
    # url(r'^adoptaschool/', include('adoptaschool.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
