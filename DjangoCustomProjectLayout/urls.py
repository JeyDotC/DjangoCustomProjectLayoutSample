from django.conf.urls import patterns, include, url
from django_utils.urls import convention_urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'DjangoCustomProjectLayout.my_app.controllers.HelloWorldController.index', name='home'),
    ('', convention_urls(root_namespace="DjangoCustomProjectLayout"))
    # Examples:
    # url(r'^DjangoCustomProjectLayout/', include('DjangoCustomProjectLayout.DjangoCustomProjectLayout.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)