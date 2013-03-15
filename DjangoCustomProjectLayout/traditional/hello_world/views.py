from ...django_utils.traditional import view
from django.views.decorators.http import require_GET

@require_GET
def index(request):
    return view(index)

@require_GET
def another_page(request):
    return view(another_page, { "content": "Foo content!" })

def a_shared_view(request):
    """
    As this view is not at this' controller's views folder,
    it'll be looked up at the Shared/ folder
    """
    return view(a_shared_view)

def shared_view(request):
    """
    Same as above but as function's name doesn't coincide with
    the template's name, we use the template= parameter. 
    """
    return view(shared_view, template="a_shared_view")