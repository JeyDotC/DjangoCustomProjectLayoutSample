from django.conf.urls import url, patterns, include

class BootstrapConvention:
    def patterns(self):
        """
        Implementor must return the url patterns
        recognized by this convention.
        """

    def run(self, request, *args, **kwargs):
        """
        This is the bootstrap method, all the requests
        that match one of the patterns above will be sent
        to here. 

        Implementor must resolve the module that will finally handle
        the request and return it's result
        """

    def urls(self):
        front_view_run = self.run
        controllers = [url(pattern, front_view_run) for pattern in self.patterns()]
        return include(patterns('', *controllers))

    def _get_module_by_name(self, module_name):
        """
        Utility method that gets a module based
        on its fully qualified name.
        """
        parts = module_name.split('.')
        m = __import__( module_name )
        for comp in parts[1:]:
            m = getattr(m, comp)            
        return m
