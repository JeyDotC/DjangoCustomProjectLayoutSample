from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import select_template 
from django.http import HttpResponse

from convention import BootstrapConvention

class TraditionalConvention(BootstrapConvention):

    def __init__(self, rootNamespace):
        self._rootNamespace = rootNamespace

    def patterns(self):
        return [
                    r'^(?P<app_name>[a-zA-Z_]\w*)/(?P<method_name>[a-zA-Z_]\w*)(/[a-zA-Z_0-9]\w*)', 
                    r'^(?P<app_name>[a-zA-Z_]\w*)/(?P<method_name>[a-zA-Z_]\w*)', 
                    r'^(?P<app_name>[a-zA-Z_]\w*)', 
                ]

    def run(self, request, app_name, method_name = "index", *args, **kwargs):
        controller = self._get_module_by_name("%s.%s.views" % 
                                            (self._rootNamespace, app_name))

        responder = getattr(controller, method_name, controller.index)
        responder.request = request
        return responder(request, *args, **kwargs)

def view(view_function, context = {}, template = None):
    t = view_function.func_name if template is None else template;
    return HttpResponse(select_template((
                                "%s.html" % t,
                            )).render(RequestContext(view_function.request, context)))