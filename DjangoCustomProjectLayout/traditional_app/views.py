from ..django_utils.traditional import view
from django.views.decorators.http import require_GET

@require_GET
def index(request):
    return view(index)

@require_GET
def another_page(request):
    return view(another_page, { "content": "Foo content!" })