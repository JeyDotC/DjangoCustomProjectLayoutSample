from django.conf.urls import url, patterns, include

class BootstrapConvention:
    """
    A class to represent a convention.

    This is a class intended to ease the implementation
    of the front controller pattern which is the core of the
    conventions mechanism.
    """

    def patterns(self):
        """
        Returns the list of regular expressions 
        recognized by this convention.
        """

    def run(self, request, *args, **kwargs):
        """
        This is the bootstrap method, all the requests
        that match one of the patterns of self.patterns()
        will be sent to here. 

        Implementor must resolve the module that will finally handle
        the request and return it's result by calling it.
        """

    def urls(self):
        """
        This method configures the urls based on the patterns returned by self.patterns().

        Returns the configured urls.
        """
        front_view_run = self.run
        controllers = [url(pattern, front_view_run) for pattern in self.patterns()]
        return include(patterns('', *controllers))

    def _get_module_by_name(self, module_name):
        """
        Utility method that gets a module based
        on its fully qualified name.

        Returns a module object.
        """
        parts = module_name.split('.')
        m = __import__( module_name )
        for comp in parts[1:]:
            m = getattr(m, comp)            
        return m
