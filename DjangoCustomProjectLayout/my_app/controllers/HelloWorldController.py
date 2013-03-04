from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_GET

@require_GET
def index(request):
    return render_to_response("HelloWorld/index.html", {},
                          context_instance=RequestContext(request) )

@require_GET
def another_page(request):
    return render_to_response("HelloWorld/another_page.html", { "content": "Foo content!" },
                          context_instance=RequestContext(request) )