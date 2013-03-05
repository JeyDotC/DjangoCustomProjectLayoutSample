from ...django_utils.net_mvc import view
from django.views.decorators.http import require_GET
from ..models.hello import Hello

@require_GET
def index(request):
    test = Hello.objects.all()
    return view(index)

@require_GET
def another_page(request):
    return view(another_page, { "content": "Foo content!" })