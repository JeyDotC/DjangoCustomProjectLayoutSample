from ...django_utils.net_mvc import view
from django.views.decorators.http import require_GET, require_POST

@require_GET
def index(request):
    return view(index)

@require_POST
def action(request):
    return view(action, {'action': request.POST["what"]})

@require_GET
def other_template(request):
    return view(other_template, template="index")

