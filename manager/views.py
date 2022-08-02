from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        template = loader.get_template("home.html")
        context = {
            'title': "Home"
        }
        return HttpResponse(template.render(context, request))