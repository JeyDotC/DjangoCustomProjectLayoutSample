from django.conf.urls import url, patterns, include
from front_view import FrontView
import re

def convention_urls(root_namespace):
    front_view_run = FrontView(root_namespace).run
    controllers = patterns('',
                    url(r'^(?P<app_name>[a-zA-Z_]\w*)/(?P<controller_name>[a-zA-Z_]\w*)/(?P<method_name>[a-zA-Z_]\w*)(/[a-zA-Z_0-9]\w*)', 
                    front_view_run, 
                    name='home'),

                    url(r'^(?P<app_name>[a-zA-Z_]\w*)/(?P<controller_name>[a-zA-Z_]\w*)/(?P<method_name>[a-zA-Z_]\w*)', 
                    front_view_run, 
                    name='home'),

                    url(r'^(?P<app_name>[a-zA-Z_]\w*)/(?P<controller_name>[a-zA-Z_]\w*)', 
                    front_view_run, 
                    name='home'))

    return include(controllers)