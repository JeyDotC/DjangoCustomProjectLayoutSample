from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import select_template 
from django.http import HttpResponse

from convention import BootstrapConvention

class NetMvcConvention(BootstrapConvention):
    """
    The .NET MVC-like implementation of BootstrapConvention.

    By using this convention, an application will have a .net mvc 
    project layout:

    rootNamespace/
        app1/
            models/
                __init__.py
                nodel1.py
                nodel2.py
            views/
                Name1/
                    index.html
                    other.html
                Name2/
                    a_view.html
                Shared/
                    layout.html
            controllers/
                Name1Controller.py
                Name2Controller.py
            __init__.py
            tests.py
    """
    def __init__(self, rootNamespace):
        self._rootNamespace = rootNamespace

    def patterns(self):
        return [
                    r'^(?P<app_name>[a-zA-Z_]\w*)/(?P<controller_name>[a-zA-Z_]\w*)/(?P<method_name>[a-zA-Z_]\w*)(/[a-zA-Z_0-9]\w*)', 
                    r'^(?P<app_name>[a-zA-Z_]\w*)/(?P<controller_name>[a-zA-Z_]\w*)/(?P<method_name>[a-zA-Z_]\w*)', 
                    r'^(?P<app_name>[a-zA-Z_]\w*)/(?P<controller_name>[a-zA-Z_]\w*)', 
                ]

    def run(self, request, app_name, controller_name, method_name = "index", *args, **kwargs):
        controller = self._get_module_by_name("%s.%s.controllers.%sController" % 
                                            (self._rootNamespace, app_name, controller_name))

        responder = getattr(controller, method_name, controller.index)
        responder.controller_name = controller_name
        view.request = request
        return responder(request, *args, **kwargs)

def view(view_function, context = {}, template = None):
    t = view_function.func_name if template is None else template;
    return HttpResponse(select_template((
                                "%s/%s.html" % (view_function.controller_name, t),
                                "Shared/%s.html" % t,
                            )).render(RequestContext(view.request, context)))