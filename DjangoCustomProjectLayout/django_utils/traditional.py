from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import select_template 
from django.http import HttpResponse

from convention import BootstrapConvention

class TraditionalConvention(BootstrapConvention):
    """
    The traditional implementation of BootstrapConvention.

    By using this convention, an application will have a typical
    django project layout:

    rootNamespace/
        app1/
          templates/
            index.html
            other.html
          __init__.py
          models.py
          tests.py
          views.py
        app2/
          templates/
            a_view.html
          __init__.py
          models.py
          tests.py
          views.py
        __init__.py

    """

    def __init__(self, rootNamespace):
        """
        Creates a new TraditionalConvention object

        rootNamespace -- A string with the root namespace name.

        """
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
        view.request = request
        view.app_name = app_name
        return responder(request, *args, **kwargs)

def view(view_function, context = {}, template = None):
    """
    An optional shorcut to render a template, the template file is
    resolved from the calling method name.

    view_function -- The function that calls this function
    context = {} -- An object representing the context data
    template = None -- An optional template name to be used instead of the funcition's name
    
    Returns an HttpResponse 
    """
    t = view_function.func_name if template is None else template;
    return HttpResponse(select_template((
                                "%s/Templates/%s.html" % (view.app_name, t),
                                "shared/Templates/%s.html" % t,
                            )).render(RequestContext(view.request, context)))