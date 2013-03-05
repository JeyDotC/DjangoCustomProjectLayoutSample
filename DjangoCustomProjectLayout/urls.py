from django.conf.urls import patterns, include, url
from django_utils.net_mvc import NetMvcConvention
from django_utils.traditional import TraditionalConvention

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

net_mvc_convention = NetMvcConvention(rootNamespace="DjangoCustomProjectLayout")

urlpatterns = patterns('',
    url(r'^$', net_mvc_convention.run, kwargs = {'app_name':'my_app', 'controller_name':'HelloWorld', 'method_name':'index'}),
    (r'^NetMVC/', net_mvc_convention.urls()),
    (r'^Traditional/', TraditionalConvention('DjangoCustomProjectLayout').urls())
    # Examples:
    # url(r'^DjangoCustomProjectLayout/', include('DjangoCustomProjectLayout.DjangoCustomProjectLayout.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)