from django.conf.urls import patterns, include, url
from django_utils.net_mvc import NetMvcConvention
from django_utils.traditional import TraditionalConvention

net_mvc_convention = NetMvcConvention(rootNamespace="DjangoCustomProjectLayout")
traditional_convention = TraditionalConvention(rootNamespace='DjangoCustomProjectLayout.traditional')

urlpatterns = patterns('',
    url(r'^$', net_mvc_convention.run, kwargs = {'app_name':'NetMVC', 'controller_name':'HelloWorld', 'method_name':'index'}),
    #The 'NetMVC/' and 'traditional/' url groupings are optional, I use them to avoid collitions due to
    #the generic nature of the urls given by the two conventions used here.
    (r'^NetMVC/', net_mvc_convention.urls()),
    (r'^traditional/', traditional_convention.urls())
)