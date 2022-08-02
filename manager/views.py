from django.http import HttpResponse
from django.template import loader

def login(request):
    template = loader.get_template("base.html")
    context = {
        'title' : "Login"
    }
    return HttpResponse(template.render(context, request))