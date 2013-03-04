class FrontView:
    def __init__(self, rootNamespace):
        self._rootNamespace = rootNamespace

    def _get_module(self, module_name):
        parts = module_name.split('.')
        m = __import__( module_name )
        for comp in parts[1:]:
            m = getattr(m, comp)            
        return m

    def run(self, request, app_name, controller_name, method_name = "index", *args, **kwargs):
        controller = self._get_module("%s.%s.controllers.%sController" % 
                                (self._rootNamespace, app_name, controller_name))
        responder = getattr(controller, method_name, controller.index)
        return responder(request, *args, **kwargs)